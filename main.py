from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

ds = pd.read_csv("topics.csv")

for index, row in ds.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=25)
    pdf.set_text_color(10, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    for y in range(20, 289, 10):
        pdf.line(10, y , 200, y)

    # FOOTER
    pdf.ln(265)
    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # FOOTER
        pdf.ln(277)
        pdf.set_font(family="Times", style="B", size=8)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)
        for y in range(20, 289, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")
