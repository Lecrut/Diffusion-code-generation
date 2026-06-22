class TruthTableGenerator:
    def __init__(self):
        self.variables = ['A', 'B', 'C']

    def generate(self):
        rows = []
        header = ' | '.join(self.variables) + ' | Result'
        rows.append(header)
        rows.append('-' * len(header))
        
        for i in range(8):
            a = (i >> 2) & 1
            b = (i >> 1) & 1
            c = (i >> 0) & 1
            result = a and b and c
            row = f"{a} | {b} | {c} | {result}"
            rows.append(row)
        return '\n'.join(rows)

if __name__ == '__main__':
    generator = TruthTableGenerator()
    print(generator.generate())