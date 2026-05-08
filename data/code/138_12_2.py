class TruthTableGenerator:
    def generate_truth_table(self, inputs):
        if not isinstance(inputs, list) or not inputs:
            return "Error: Input must be a non-empty list of boolean values."
        num_inputs = len(inputs)
        num_rows = 2**num_inputs
        truth_table = []
        for i in range(num_rows):
            row = []
            for j in range(num_inputs):
                if (i >> j) & 1:
                    row.append(str(inputs[j]))
                else:
                    row.append(str(not inputs[j]))
            truth_table.append(row)
        header = [f"Input {j+1}" for j in range(num_inputs)]
        header.append("Output")
        table_output = []
        table_output.append(header)
        for row in truth_table:
            table_output.append(row)
        return table_output
if __name__ == '__main__':
    generator = TruthTableGenerator()
    sample_inputs = [False, True]
    print("--- Truth Table for [False, True] ---")
    result = generator.generate_truth_table(sample_inputs)
    for row in result:
        print(" ".join(row))
    print("\n--- Truth Table for [True, False, True] ---")
    sample_inputs_2 = [True, False, True]
    result_2 = generator.generate_truth_table(sample_inputs_2)
    for row in result_2:
        print(" ".join(row))