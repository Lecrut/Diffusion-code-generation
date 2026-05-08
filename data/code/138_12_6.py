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
        header = list(inputs)
        header.append("Result")
        output.insert(0, header)
        return output
if __name__ == '__main__':
    generator = TruthTableGenerator()
    sample_inputs = [False, True]
    truth_table = generator.generate_truth_table(sample_inputs)
    for row in truth_table:
        print(" ".join(map(str, row)))