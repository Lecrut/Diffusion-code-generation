class XorTruthTableGenerator:
    def __init__(self):
        self.inputs = [0, 1]

    def compute_row(self, a, b):
        return a ^ b

    def generate_all_rows(self):
        rows = []
        for a in self.inputs:
            for b in self.inputs:
                result = self.compute_row(a, b)
                rows.append((a, b, result))
        return rows

    def format_row(self, row):
        a, b, out = row
        return f"{a} XOR {b} = {out}"

if __name__ == '__main__':
    generator = XorTruthTableGenerator()
    rows = generator.generate_all_rows()
    for row in rows:
        formatted = generator.format_row(row)
        print(formatted)