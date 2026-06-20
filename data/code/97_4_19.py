class BinaryTruthTable:
    def __init__(self):
        self.variables = ['P', 'Q']
        self.combinations = [(False, False), (False, True), (True, False), (True, True)]

    def generate_truth_table(self):
        table = []
        for p, q in self.combinations:
            row = {var: p if var == 'P' else q for var in self.variables}
            row['P -> Q'] = not p or q
            table.append(row)
        return table

if __name__ == '__main__':
    generator = BinaryTruthTable()
    truth_table = generator.generate_truth_table()
    for row in truth_table:
        print(f"{row['P']} | {row['Q']} | {row['P -> Q']}")