class TruthTableGenerator:
    def __init__(self):
        self.combinations = [(a, b) for a in [0, 1] for b in [0, 1]]

    def generate_truth_table(self):
        truth_table = []
        for a, b in self.combinations:
            result = 'T' if not a or b else 'F'
            truth_table.append((a, b, result))
        return truth_table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    truth_table = generator.generate_truth_table()
    for row in truth_table:
        print(row)