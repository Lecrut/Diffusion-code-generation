class TruthTableGenerator:
    def __init__(self):
        self.variables = ['A', 'B', 'C']

    def generate(self):
        rows = []
        header = " | ".join(self.variables)
        rows.append(header)
        rows.append("-" * len(header))
        for i in range(8):
            a = (i >> 2) & 1
            b = (i >> 1) & 1
            c = (i >> 0) & 1
            row_str = f"{a} | {b} | {c}"
            rows.append(row_str)
        return "\n".join(rows)

if __name__ == '__main__':
    generator = TruthTableGenerator()
    print(generator.generate())