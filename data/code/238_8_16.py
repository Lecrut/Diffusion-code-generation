from reportlab.pdfgen import canvas

def create_pdf_canvas():
    c = canvas.Canvas("output.pdf")
    c.setFillColorRGB(0, 0, 0)
    c.rect(50, 50, 100, 100, fill=True)
    return c

if __name__ == '__main__':
    pdf_canvas = create_pdf_canvas()
    print(pdf_canvas)