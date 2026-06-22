class StarSquare:
    def __init__(self, size=9):
        self.size = size

    def build_row(self):
        row_chars = []
        index = 0
        while index < self.size:
            row_chars.append("*")
            index += 1
        return "".join(row_chars)

    def render(self):
        lines = []
        r = 0
        while r < self.size:
            lines.append(self.build_row())
            r += 1
        return "\n".join(lines)

def generate_star_square(size=9):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")
    square = StarSquare(size)
    return square.render()

if __name__ == '__main__':
    instance = StarSquare(9)
    print(instance.render())
    print(instance.build_row())