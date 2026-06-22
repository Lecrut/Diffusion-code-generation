from reportlab.pdfgen import canvas

def create_pdf_with_rectangle():
    c = canvas.Canvas("output.pdf")
    rectangle_position = (50, 50)
    rectangle_dimensions = (100, 100)
    c.rect(*rectangle_position, *rectangle_dimensions, fill=True, stroke=False, fillColor="black")
    return c

if __name__ == '__main__':
    pdf_canvas = create_pdf_with_rectangle()
    print(pdf_canvas)