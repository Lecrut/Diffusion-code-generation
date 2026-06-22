import cairo

def create_pdf_with_box():
    surface = cairo.PDFSurface('output.pdf', 200, 200)
    context = cairo.Context(surface)
    colors = {'blue': (0, 0, 1)}
    color_name = 'blue'
    context.set_source_rgb(*colors[color_name])
    context.rectangle(0, 0, 200, 200)
    context.fill()
    return context

if __name__ == '__main__':
    context = create_pdf_with_box()
    print(context)