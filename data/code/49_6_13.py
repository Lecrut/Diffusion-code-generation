class StarSquarePrinter:
    def __init__(self, size):
        self._validate_size(size)
        self.size = size

    def _validate_size(self, size):
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Size must be a positive integer")

    def print_square(self):
        line_content = '*' * self.size
        for _ in range(self.size):
            print(line_content)

if __name__ == '__main__':
    printer = StarSquarePrinter(10)
    printer.print_square()