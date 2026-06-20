class TruthTableGenerator:
    def generate_truth_table(self):
        table = []
        for a in [0, 1]:
            for b in [0, 1]:
                row = {'A': a, 'B': b}
                row['NOT A'] = not a
                row['NOT B'] = not b
                row['A AND B'] = a and b
                row['A OR B'] = a or b
                row['A XOR B'] = a != b
                table.append(row)
        return table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    truth_table = generator.generate_truth_table()
    for row in truth_table:
        print(row)