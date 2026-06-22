class StarSquarePrinter:
    BORDER = '*'
    SPACE = ' '

    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 1:
            raise ValueError("Size must be a positive integer")
        self.size = size

    def get_row(self, index):
        if index == 0 or index == self.size - 1:
            return self.BORDER * self.size
        else:
            return self.BORDER + self.SPACE * (self.size - 2) + self.BORDER

    def generate(self):
        lines = []
        for i in range(self.size):
            lines.append(self.get_row(i))
        return "\n".join(lines)

def print_star_square(size):
    try:
        printer = StarSquarePrinter(size)
        result = printer.generate()
        print(result)
        return result
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    print_star_square(1)
    print("---")
    print_star_square(5)
    print("---")
    print_star_square(3)
    print("---")
    print_star_square(-2)