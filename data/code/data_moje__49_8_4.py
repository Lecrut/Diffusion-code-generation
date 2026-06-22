class StarSquarePrinter:
    def __init__(self, size):
        self.size = size

    def render(self):
        row = 0
        while row < self.size:
            col = 0
            line = ""
            while col < self.size:
                line += "*"
                col += 1
            print(line)
            row += 1
        return self.size

    def get_dimensions(self):
        return self.size, self.size

if __name__ == '__main__':
    printer = StarSquarePrinter(9)
    printed_size = printer.render()
    width, height = printer.get_dimensions()