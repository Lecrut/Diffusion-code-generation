class StarSquarePrinter:
    def __init__(self, dimension):
        self.dimension = dimension

    def draw(self):
        row_content = '*' * self.dimension
        for index in range(self.dimension):
            print(row_content)

if __name__ == '__main__':
    side_length = 10
    printer = StarSquarePrinter(side_length)
    printer.draw()