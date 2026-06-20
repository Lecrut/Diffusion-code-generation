class TruthTableGenerator:
    def generate_and_truth_table(self):
        inputs = [True, False]
        results = []
        for a in inputs:
            for b in inputs:
                result = a and b
                results.append((a, b, result))
        return results

if __name__ == '__main__':
    generator = TruthTableGenerator()
    truth_table = generator.generate_and_truth_table()
    for row in truth_table:
        print(f"{row[0]} AND {row[1]} = {row[2]}")