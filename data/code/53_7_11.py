class ReverseNumberTrianglePrinter:
    def __init__(self, row_count):
        if not isinstance(row_count, int) or row_count <= 0:
            raise ValueError("Row count must be a positive integer")
        self.row_count = row_count

    def generate(self):
        lines = []
        for current_row in range(self.row_count, 0, -1):
            numbers = []
            for num in range(1, current_row + 1):
                numbers.append(str(num))
            lines.append(" ".join(numbers))
        return "\n".join(lines)

if __name__ == '__main__':
    printer = ReverseNumberTrianglePrinter(6)
    print(printer.generate())