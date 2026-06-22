import cairo

def create_pdf_with_box():
    if not isinstance(200, (int, float)) or 200 <= 0:
        raise ValueError('Width and height must be positive numbers')
    surface = cairo.PDFSurface('output.pdf', 200, 200)
    context = cairo.Context(surface)
    context.set_source_rgb(0, 0, 1)
    context.rectangle(0, 0, 200, 200)
    context.fill()
    return context
if __name__ == '__main__':
    try:
        context = create_pdf_with_box()
        print(context)
    except ValueError as e:
        print(e)