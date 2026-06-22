import cairo

class PDFBoxDrawer:
    BOX_WIDTH = 200
    BOX_HEIGHT = 200
    BLUE_COLOR = (0, 0, 1)

    @staticmethod
    def create_pdf_with_box():
        surface = cairo.PDFSurface('output.pdf', PDFBoxDrawer.BOX_WIDTH, PDFBoxDrawer.BOX_HEIGHT)
        context = cairo.Context(surface)
        context.set_source_rgb(*PDFBoxDrawer.BLUE_COLOR)
        context.rectangle(0, 0, PDFBoxDrawer.BOX_WIDTH, PDFBoxDrawer.BOX_HEIGHT)
        context.fill()
        return context

if __name__ == '__main__':
    context = PDFBoxDrawer.create_pdf_with_box()
    print(context)