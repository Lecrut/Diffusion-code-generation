from reportlab.pdfgen import canvas

def create_pdf_with_rectangle():
    c = canvas.Canvas('output.pdf')
    x, y = (50, 50)
    width, height = (100, 100)
    c.setFillColorRGB(0, 0, 0)
    c.rect(x, y, width, height, fill=True)
    return c
if __name__ == '__main__':
    pdf_canvas = create_pdf_with_rectangle()
    print(pdf_canvas)