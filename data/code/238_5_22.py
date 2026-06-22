import cairo

def create_pdf_with_box():
    surface = cairo.PDFSurface('output.pdf', 300, 300)
    context = cairo.Context(surface)
    context.set_source_rgb(0, 0, 1)
    context.rectangle(50, 50, 200, 200)
    context.fill()
    return context
if __name__ == '__main__':
    context = create_pdf_with_box()
    print(context)