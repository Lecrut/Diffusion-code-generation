import itertools

class TruthTableBuilder:
    def __init__(self, variables):
        self.variables = variables
        self.n = len(variables)

    def build_truth_table(self):
        truth_values = list(itertools.product([False, True], repeat=self.n))
        table = {}
        for row in truth_values:
            key = tuple(row)
            values = {var: val for var, val in zip(self.variables, row)}
            table[key] = values
        return table

    def print_truth_table(self):
        table = self.build_truth_table()
        header = ' | '.join(self.variables)
        print(header)
        print('-' * len(header))
        for key, values in table.items():
            row = ' | '.join(str(values[var]) for var in self.variables)
            print(row)

if __name__ == '__main__':
    builder = TruthTableBuilder(["A", "B"])
    builder.print_truth_table()