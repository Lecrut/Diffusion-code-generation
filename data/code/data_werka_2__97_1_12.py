class TruthTableGenerator:
    DEFAULT_VARS = ('A', 'B', 'C')

    def __init__(self, variables=None):
        if variables is None:
            variables = self.DEFAULT_VARS
        self.variables = tuple(variables)
        self.num_vars = len(self.variables)

    def _get_bits(self, index):
        bits = []
        mask = 1 << (self.num_vars - 1)
        for _ in range(self.num_vars):
            bits.append(bool(index & mask))
            index <<= 1
        return bits

    def generate_rows(self):
        total = 1 << self.num_vars
        rows = []
        for i in range(total):
            bits = self._get_bits(i)
            row = {self.variables[j]: bits[j] for j in range(self.num_vars)}
            rows.append(row)
        return rows

    def display(self):
        rows = self.generate_rows()
        header = ' | '.join(self.variables) + ' | Result'
        print(header)
        print('-' * len(header))
        for row in rows:
            values = [str(int(row[v])) for v in self.variables]
            val_a, val_b, val_c = [row[v] for v in self.variables]
            result = val_a and val_b and val_c
            values.append(str(int(result)))
            print(' | '.join(values))

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.display()