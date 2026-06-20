class TruthTable:

    def __init__(self, outputs):
        self.outputs = outputs

    def get_truth_table(self):
        n = len(self.outputs)
        num_inputs = n.bit_length() - 1
        truth_table = []
        for i in range(2 ** num_inputs):
            input_values = [i >> j & 1 for j in range(num_inputs)]
            output_value = self.outputs[i]
            truth_table.append((input_values, output_value))
        return truth_table
if __name__ == '__main__':
    outputs = [0, 1, 1, 0]
    tt = TruthTable(outputs)
    print(tt.get_truth_table())