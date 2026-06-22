import cairo
BOX_WIDTH = 200
BOX_HEIGHT = 200
OUTPUT_FILE = 'output.pdf'

def create_pdf_with_box():
    surface = cairo.PDFSurface(OUTPUT_FILE, BOX_WIDTH, BOX_HEIGHT)
    context = cairo.Context(surface)
    context.set_source_rgb(0, 0, 1)
    context.rectangle(0, 0, BOX_WIDTH, BOX_HEIGHT)
    context.fill()
    return context
if __name__ == '__main__':
    context = create_pdf_with_box()
    print(context)