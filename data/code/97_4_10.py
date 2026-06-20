class TruthTableGenerator:
    def generate_truth_table(self):
        truth_table = []
        for a in [0, 1]:
            for b in [0, 1]:
                row = {'a': a, 'b': b}
                row['not_a'] = not a
                row['and_ab'] = a and b
                row['or_ab'] = a or b
                row['xor_ab'] = a != b
                truth_table.append(row)
        return truth_table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    table = generator.generate_truth_table()
    for row in table:
        print(row)