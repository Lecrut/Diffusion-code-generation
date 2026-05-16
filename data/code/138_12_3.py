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
        output = []
        output.append(header)
        for row in truth_table:
            output.append(row)
        return output
if __name__ == '__main__':
    generator = TruthTableGenerator()
    sample_inputs = [False, True]
    truth_table_data = generator.generate_truth_table(sample_inputs)
    print("--- Truth Table for Inputs:", sample_inputs)
    for row in truth_table_data:
        print(" | ".join(row))
    print("\n--- Another Example (3 inputs):")
    sample_inputs_2 = [True, False, True]
    truth_table_data_2 = generator.generate_truth_table(sample_inputs_2)
    header_2 = [f"Input {j+1}" for j in range(len(sample_inputs_2))]
    header_2.append("Output")
    print("Header:", header_2)
    for row in truth_table_data_2:
        print(" | ".join(row))