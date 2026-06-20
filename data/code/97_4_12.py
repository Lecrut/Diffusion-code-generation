class BinaryTruthTable:
    def __init__(self):
        self.variables = ['P', 'Q']
        self.values = [False, True]

    def generate_truth_table(self):
        table = []
        for p in self.values:
            for q in self.values:
                row = {var: p if var == 'P' else q for var in self.variables}
                row['P -> Q'] = not p or q
                table.append(row)
        return table

    def print_truth_table(self):
        table = self.generate_truth_table()
        print("P | Q | P -> Q")
        print("---|---|------")
        for row in table:
            print(f"{row['P']} | {row['Q']} | {row['P -> Q']}")

if __name__ == '__main__':
    generator = BinaryTruthTable()
    generator.print_truth_table()