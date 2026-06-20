class LogicTableGenerator:
    def generate_and_truth_table(self, inputs):
        results = []
        for a in inputs:
            for b in inputs:
                and_result = a and b
                results.append((a, b, and_result))
        return results

if __name__ == '__main__':
    generator = LogicTableGenerator()
    sample_inputs = [True, False]
    truth_table = generator.generate_and_truth_table(sample_inputs)
    for row in truth_table:
        print(f"{row[0]} AND {row[1]} = {row[2]}")