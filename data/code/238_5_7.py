import cairo

def create_pdf_with_box():
    surface = cairo.PDFSurface('output.pdf', 200, 200)
    context = cairo.Context(surface)
    colors = {'blue': (0, 0, 1)}
    context.set_source_rgb(*colors['blue'])
    context.rectangle(0, 0, 200, 200)
    context.fill()
    return context

if __name__ == '__main__':
    context = create_pdf_with_box()
    print(context)