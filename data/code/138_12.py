class TruthTableGenerator:
    def generate_truth_table(self, inputs):
        if not isinstance(inputs, list) or not inputs:
            return "Error: Input must be a non-empty list of boolean values."
        num_inputs = len(inputs)
        num_rows = 2 ** num_inputs
        table = []
        for i in range(num_rows):
            row = []
            for j in range(num_inputs):
                if (i >> j) & 1:
                    row.append(str(inputs[j]))
                else:
                    row.append(str(not inputs[j]))
            table.append(row)
        header = [str(x) for x in inputs]
        result = [header] + table
        return result
if __name__ == '__main__':
    generator = TruthTableGenerator()
    sample_inputs = [False, True]
    truth_table = generator.generate_truth_table(sample_inputs)
    print("Truth Table for inputs:", sample_inputs)
    for row in truth_table:
        print(" ".join(row))
    print("\n--- Another Example (3 inputs) ---")
    sample_inputs_2 = [True, False, True]
    truth_table_2 = generator.generate_truth_table(sample_inputs_2)
    print("Truth Table for inputs:", sample_inputs_2)
    for row in truth_table_2:
        print(" ".join(row))