class TruthTableGenerator:
    def generate_truth_table(self, inputs):
        if not isinstance(inputs, list) or not inputs:
            return "Error: Input must be a non-empty list of boolean values."
        n = len(inputs)
        output = []
        for i in range(2**n):
            row = []
            temp = i
            for j in range(n):
                row.append(bool(temp % 2))
                temp //= 2
            output.append(row)
        return output
    def display_truth_table(self, inputs):
        truth_table = self.generate_truth_table(inputs)
        if isinstance(truth_table, str):
            print(truth_table)
            return
        n = len(inputs)
        if n == 0:
            return
        header = [f"Input {i+1}" for i in range(n)]
        print("--- Truth Table ---")
        print(" | ".join(header))
        print("-" * (len(header) * 4 + 1))
        for row in truth_table:
            print(" | ".join(map(str, row)))
        print("-" * (len(header) * 4 + 1))
if __name__ == '__main__':
    generator = TruthTableGenerator()
    sample_inputs = [False, True]
    print("Generating truth table for inputs:", sample_inputs)
    generator.display_truth_table(sample_inputs)
    sample_inputs_2 = [False, False, True]
    print("\nGenerating truth table for inputs:", sample_inputs_2)
    generator.display_truth_table(sample_inputs_2)
    sample_inputs_3 = [True, False, True, False]
    print("\nGenerating truth table for inputs:", sample_inputs_3)
    generator.display_truth_table(sample_inputs_3)