import cairo

def create_pdf_with_box():
    width = 200
    height = 200
    surface = cairo.PDFSurface('output.pdf', width, height)
    if not isinstance(surface, cairo.Surface):
        raise ValueError('Failed to create PDF surface')
    context = cairo.Context(surface)
    if not isinstance(context, cairo.Context):
        raise ValueError('Failed to create Cairo context')
    context.set_source_rgb(0, 0, 1)
    context.rectangle(0, 0, width, height)
    context.fill()
    return context
if __name__ == '__main__':
    context = create_pdf_with_box()
    print(context)