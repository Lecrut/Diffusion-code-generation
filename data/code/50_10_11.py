class StarTrianglePrinter:
    def __init__(self, height):
        self.height = height
        self._lines = []

    def _compute_rows(self):
        lines = []
        for i in range(1, self.height + 1):
            line = '*' * i
            lines.append(line)
        self._lines = lines

    def render(self):
        self._compute_rows()
        for line in self._lines:
            print(line)

    def get_lines(self):
        if not self._lines:
            self._compute_rows()
        return self._lines

def print_right_angled_triangle(height):
    printer = StarTrianglePrinter(height)
    printer.render()
    return printer.get_lines()

if __name__ == '__main__':
    sample_height = 6
    result_lines = print_right_angled_triangle(sample_height)
    print(result_lines)