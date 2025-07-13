import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# 🔸 Read data from CSV
data = pd.read_csv("ansh_data.csv")  # Make sure this matches your file name

# 🔸 Analyze data
total_entries = len(data)
average_value = data.select_dtypes(include='number').mean().mean()
max_value = data.select_dtypes(include='number').max().max()
min_value = data.select_dtypes(include='number').min().min()

# 🔸 PDF setup
output_file = "Automated_Report.pdf"
styles = getSampleStyleSheet()
elements = []

# 🔸 Report content
elements.append(Paragraph("<b>CODTECH INTERNSHIP TASK - 2</b>", styles['Title']))
elements.append(Paragraph("<b>AUTOMATED REPORT GENERATION</b>", styles['Heading2']))
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>INSTRUCTIONS:</b>", styles['Heading3']))
elements.append(Paragraph("• Develop a script that reads data from a file, analyzes it, and generates a formatted PDF report using libraries like FPDF or ReportLab.", styles['Normal']))
elements.append(Paragraph("• Deliverable: A script and a sample report.", styles['Normal']))
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>Sample Data Analysis:</b>", styles['Heading3']))
table_data = [
    ['Metric', 'Value'],
    ['Total Entries', str(total_entries)],
    ['Average Value', f"{average_value:.2f}"],
    ['Max Value', str(max_value)],
    ['Min Value', str(min_value)]
]
table = Table(table_data, colWidths=[200, 200])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
]))
elements.append(table)
elements.append(Spacer(1, 20))

elements.append(Paragraph("<b>Note:</b> Completion certificate will be issued on your internship end date.", styles['Normal']))
elements.append(Spacer(1, 40))
elements.append(Paragraph("Submitted By: Himesh Kumar Gupta<br/>CodTech Internship", styles['Normal']))

# 🔸 Watermark function
def add_watermark(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica-Bold', 36)
    canvas.setFillColorRGB(0.85, 0.85, 0.85)  # Light gray
    canvas.rotate(45)
    canvas.drawCentredString(400, 0, "Himesh Kumar Gupta")  # Watermark text
    canvas.restoreState()

# 🔸 Generate PDF with watermark
doc = SimpleDocTemplate(output_file, pagesize=A4)
doc.build(elements, onFirstPage=add_watermark, onLaterPages=add_watermark)

print("✅ PDF generated with watermark: Himesh Kumar Gupta")