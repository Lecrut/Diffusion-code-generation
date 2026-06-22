class StarSquarePrinter:
    SIDE_LENGTH = 5

    @staticmethod
    def _build_row(length):
        return '*' * length

    def generate_pattern(self):
        row = self._build_row(self.SIDE_LENGTH)
        lines = [row for _ in range(self.SIDE_LENGTH)]
        return '\n'.join(lines)

if __name__ == '__main__':
    printer = StarSquarePrinter()
    print(printer.generate_pattern())