import pandas as pd
from fpdf import FPDF


df = pd.read_csv('data.csv')


summary = df.groupby('Subject')['Marks'].describe().round(2)


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)


pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Automated Student Report", ln=True, align='C')

pdf.set_font("Arial", size=12)
pdf.ln(10)


for subject in summary.index:
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt=f"Subject: {subject}", ln=True)
    
    stats = summary.loc[subject]
    for stat_name, stat_value in stats.items():
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 8, txt=f"{stat_name}: {stat_value}", ln=True)

    pdf.ln(5)

# Save PDF
pdf.output("student_report.pdf")
