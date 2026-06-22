class TrianglePrinter:
    def __init__(self, rows):
        self.rows = rows

    def _build_line(self, i):
        space_count = self.rows - i
        star_count = i
        return " " * space_count + "*" * star_count

    def get_triangle_lines(self):
        lines = []
        for i in range(1, self.rows + 1):
            lines.append(self._build_line(i))
        return lines

    def print_triangle(self):
        lines = self.get_triangle_lines()
        for line in lines:
            print(line)
        return lines

def generate_right_aligned_triangle(row_count):
    printer = TrianglePrinter(row_count)
    return printer.get_triangle_lines()

if __name__ == '__main__':
    num_rows = 10
    lines = generate_right_aligned_triangle(num_rows)
    for line in lines:
        print(line)