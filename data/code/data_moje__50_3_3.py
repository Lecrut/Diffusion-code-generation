class StarTrianglePrinter:
    def __init__(self, rows):
        if not isinstance(rows, int):
            raise TypeError("Rows must be an integer")
        if rows < 0:
            raise ValueError("Rows must be non-negative")
        self.rows = rows

    def generate(self):
        for i in range(1, self.rows + 1):
            print("*" * i)

if __name__ == "__main__":
    PRINTER = StarTrianglePrinter(15)
    PRINTER.generate()