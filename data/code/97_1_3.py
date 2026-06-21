class TruthTableGenerator:
    def __init__(self, variables=None):
        if variables is None:
            variables = ['A', 'B', 'C']
        self.variables = variables
        self.num_vars = len(variables)
        self.rows = 2 ** self.num_vars

    def _get_combinations(self):
        combinations = []
        for i in range(self.rows):
            row = []
            for j in range(self.num_vars - 1, -1, -1):
                bit = (i >> j) & 1
                row.append(bool(bit))
            combinations.append(row)
        return combinations

    def generate(self):
        combinations = self._get_combinations()
        header = self.variables[:]
        table = [header]
        for combo in combinations:
            table.append(combo)
        return table

    def display(self):
        table = self.generate()
        col_widths = []
        for i, col in enumerate(table):
            max_len = 0
            for row in table:
                val = row[i]
                if isinstance(val, bool):
                    val_str = str(val)
                else:
                    val_str = str(val)
                if len(val_str) > max_len:
                    max_len = len(val_str)
            col_widths.append(max_len)

        for i, row in enumerate(table):
            line_parts = []
            for j, val in enumerate(row):
                if isinstance(val, bool):
                    val_str = str(val)
                else:
                    val_str = str(val)
                line_parts.append(val_str.rjust(col_widths[j]))
            print(" ".join(line_parts))

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.display()