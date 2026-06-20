class TruthTableGenerator:
    def generate_truth_table(self):
        truth_table = []
        for a in [0, 1]:
            for b in [0, 1]:
                row = {'A': a, 'B': b}
                row['AND'] = a and b
                row['OR'] = a or b
                row['NOT A'] = not a
                row['NOT B'] = not b
                truth_table.append(row)
        return truth_table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    table = generator.generate_truth_table()
    for row in table:
        print(row)