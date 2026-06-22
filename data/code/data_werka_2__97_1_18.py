class TruthTableGenerator:
    def __init__(self, variables=None):
        if variables is None:
            self.variables = ['A', 'B', 'C']
        else:
            self.variables = variables

    def generate(self):
        n = len(self.variables)
        rows = []
        total = 1 << n
        for i in range(total):
            row = {}
            for j, var in enumerate(self.variables):
                bit_index = n - 1 - j
                row[var] = bool((i >> bit_index) & 1)
            rows.append(row)
        return rows

    def display(self, rows):
        header = ' | '.join(self.variables)
        print(header)
        print('-' * len(header))
        for row in rows:
            values = [str(int(row[var])) for var in self.variables]
            print(' | '.join(values))

if __name__ == '__main__':
    generator = TruthTableGenerator()
    rows = generator.generate()
    generator.display(rows)
    print(rows[0])