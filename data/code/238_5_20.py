import cairo

class PDFBoxDrawer:

    def __init__(self, filename):
        self.filename = filename

    def create_pdf_with_box(self):
        surface = cairo.PDFSurface(self.filename, 200, 200)
        context = cairo.Context(surface)
        context.set_source_rgb(0, 0, 1)
        context.rectangle(0, 0, 200, 200)
        context.fill()
        return context
if __name__ == '__main__':
    drawer = PDFBoxDrawer('output.pdf')
    context = drawer.create_pdf_with_box()
    print(context)