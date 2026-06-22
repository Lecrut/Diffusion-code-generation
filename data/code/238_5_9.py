import cairo

class PDFDrawer:
    def __init__(self):
        self.surface = cairo.PDFSurface('output.pdf', 200, 200)
        self.context = cairo.Context(self.surface)

    def set_box_color(self, r, g, b):
        self.context.set_source_rgb(r, g, b)

    def draw_filled_box(self, x, y, width, height):
        self.context.rectangle(x, y, width, height)
        self.context.fill()

if __name__ == '__main__':
    drawer = PDFDrawer()
    drawer.set_box_color(0, 0, 1)
    drawer.draw_filled_box(0, 0, 200, 200)
    print("Box drawn successfully in output.pdf")