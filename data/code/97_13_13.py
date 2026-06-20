class TruthTableGenerator:
    def __init__(self):
        self.inputs = [True, False]

    def generate_and_truth_table(self):
        results = []
        for a in self.inputs:
            for b in self.inputs:
                and_result = a and b
                results.append((a, b, and_result))
        return results

if __name__ == '__main__':
    generator = TruthTableGenerator()
    truth_table = generator.generate_and_truth_table()
    for row in truth_table:
        print(f"{row[0]} AND {row[1]} = {row[2]}")