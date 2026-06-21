class TruthTableGenerator:

    def __init__(self, inputs):
        self.inputs = inputs

    def generate_truth_table(self):
        num_inputs = len(self.inputs)
        num_rows = 2 ** num_inputs
        truth_table = []
        for i in range(num_rows):
            input_values = []
            temp = i
            for _ in range(num_inputs):
                input_values.append(temp % 2)
                temp //= 2
            input_values.reverse()
            output = self.evaluate_expression(input_values)
            truth_table.append((input_values, output))
        return truth_table

    def evaluate_expression(self, inputs):
        A, B, C = (inputs[0], inputs[1], inputs[2])
        result = A and B or not C
        return result
if __name__ == '__main__':
    sample_inputs = [True, False, True]
    generator = TruthTableGenerator(sample_inputs)
    truth_table = generator.generate_truth_table()
    for inputs, output in truth_table:
        print(f'Inputs: {inputs}, Output: {output}')