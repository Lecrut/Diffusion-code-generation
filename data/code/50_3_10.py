class StarTriangleBuilder:
    def __init__(self, rows):
        if not isinstance(rows, int):
            raise TypeError("Rows must be an integer")
        if rows < 0:
            raise ValueError("Rows must be non-negative")
        self.rows = rows
        self._lines = []

    def build(self):
        line = ""
        for i in range(1, self.rows + 1):
            line += "*"
            self._lines.append(line)
        return self._lines

    def get_line_count(self):
        return len(self._lines)

    def get_last_line(self):
        if not self._lines:
            return ""
        return self._lines[-1]

    def print_triangle(self):
        for line in self._lines:
            print(line)

if __name__ == '__main__':
    CONST_ROWS = 15
    builder = StarTriangleBuilder(CONST_ROWS)
    builder.build()
    print(f"Total rows generated: {builder.get_line_count()}")
    print(f"Last row content length: {len(builder.get_last_line())}")
    builder.print_triangle()