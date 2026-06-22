import cairo

class PDFBoxDrawer:
    def __init__(self, width=200, height=200):
        self.width = width
        self.height = height
        self.surface = cairo.PDFSurface('output.pdf', self.width, self.height)
        self.context = cairo.Context(self.surface)

    def draw_box(self):
        self.context.set_source_rgb(0, 0, 1)
        self.context.rectangle(0, 0, self.width, self.height)
        self.context.fill()

if __name__ == '__main__':
    drawer = PDFBoxDrawer()
    drawer.draw_box()
    print(drawer.surface.get_width())
    print(drawer.surface.get_height())