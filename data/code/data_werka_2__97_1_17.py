class TruthTableGenerator:
    def __init__(self, variables=None):
        if variables is None:
            variables = ['A', 'B', 'C']
        self.variables = variables
        self.num_vars = len(variables)

    def _generate_combinations(self):
        combinations = []
        total = 2 ** self.num_vars
        for i in range(total):
            row = []
            for j in range(self.num_vars - 1, -1, -1):
                bit = (i >> j) & 1
                row.append(bool(bit))
            combinations.append(row)
        return combinations

    def generate(self):
        combinations = self._generate_combinations()
        header = self.variables + ['Result']
        table = [header]
        for row_vals in combinations:
            result = row_vals[0] and (row_vals[1] or row_vals[2])
            table.append(row_vals + [result])
        return table

    def display(self):
        table = self.generate()
        col_widths = [max(len(str(cell)) for cell in col) for col in zip(*table)]
        for i, row in enumerate(table):
            formatted_row = []
            for j, cell in enumerate(row):
                val = str(cell)
                if j < len(col_widths):
                    formatted_row.append(val.rjust(col_widths[j]))
                else:
                    formatted_row.append(val)
            print(' | '.join(formatted_row))
            if i == 0:
                print('-+-'.join('-' * w for w in col_widths))

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.display()