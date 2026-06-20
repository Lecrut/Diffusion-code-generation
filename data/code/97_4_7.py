class BinaryTruthTable:
    def __init__(self):
        self.columns = ['P', 'Q', 'P -> Q']
    
    def generate_truth_table(self):
        table = []
        for p in [False, True]:
            for q in [False, True]:
                result = not p or q
                row = {'P': p, 'Q': q, 'P -> Q': result}
                table.append(row)
        return table
    
    def print_truth_table(self):
        table = self.generate_truth_table()
        header = '|'.join(self.columns).center(15)
        separator = '-' * len(header)
        print(header)
        print(separator)
        for row in table:
            print(f"{row['P']:<4}|{row['Q']:<4}|{row['P -> Q']:>8}")

if __name__ == '__main__':
    generator = BinaryTruthTable()
    generator.print_truth_table()