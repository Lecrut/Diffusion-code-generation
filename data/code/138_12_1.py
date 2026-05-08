class TruthTableGenerator:
    def generate_truth_table(self, inputs):
        if not isinstance(inputs, list) or len(inputs) == 0:
            return "Error: Input must be a non-empty list of boolean values."
        num_inputs = len(inputs)
        num_rows = 2**num_inputs
        table = []
        for i in range(num_rows):
            row = []
            for j in range(num_inputs):
                if (i >> j) & 1:
                    row.append(True)
                else:
                    row.append(False)
            table.append(row)
        header = [f"Input {j+1}" for j in range(num_inputs)]
        table.append(header)
        return table
if __name__ == '__main__':
    generator = TruthTableGenerator()
    sample_inputs = [False, True]
    truth_table = generator.generate_truth_table(sample_inputs)
    print("Truth Table:")
    for row in truth_table:
        print(" ".join(map(str, row)))