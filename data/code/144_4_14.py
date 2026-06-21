class TruthTableGenerator:
    def __init__(self):
        self.combinations = list(itertools.product([0, 1], repeat=2))

    def generate_truth_table(self):
        truth_table = []
        for a, b in self.combinations:
            val_a = 'T' if a == 1 else 'F'
            val_b = 'T' if b == 1 else 'F'
            implication_result = 'T' if (a == 0 or b == 1) else 'F'
            truth_table.append((val_a, val_b, implication_result))
        return truth_table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    truth_table = generator.generate_truth_table()
    for row in truth_table:
        print(row)