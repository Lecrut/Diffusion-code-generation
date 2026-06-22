import cairo

def create_pdf_with_box():
    width = 200
    height = 200
    if width <= 0 or height <= 0:
        raise ValueError('Width and height must be positive integers')
    surface = cairo.PDFSurface('output.pdf', width, height)
    context = cairo.Context(surface)
    context.set_source_rgb(0, 0, 1)
    context.rectangle(0, 0, width, height)
    context.fill()
    return context
if __name__ == '__main__':
    try:
        context = create_pdf_with_box()
        print(context)
    except ValueError as e:
        print(e)