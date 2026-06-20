class TruthTableGenerator:
    INPUTS = [True, False]

    @staticmethod
    def generate_and_truth_table():
        results = []
        for a in TruthTableGenerator.INPUTS:
            for b in TruthTableGenerator.INPUTS:
                and_result = a and b
                results.append((a, b, and_result))
        return results

if __name__ == '__main__':
    truth_table = TruthTableGenerator.generate_and_truth_table()
    for row in truth_table:
        print(row)