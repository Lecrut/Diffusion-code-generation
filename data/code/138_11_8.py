class TruthTable:
    def __init__(self, outputs):
        self.outputs = outputs

    def get_truth_table(self):
        num_vars = len(bin(len(self.outputs) - 1).replace("0b", ""))
        truth_table = []
        for i in range(2 ** num_vars):
            binary = bin(i)[2:].zfill(num_vars)
            input_values = tuple(int(bit) for bit in binary)
            output_value = self.outputs[i]
            truth_table.append((input_values, output_value))
        return truth_table

if __name__ == '__main__':
    sample_outputs = [0, 1, 1, 0]
    tt = TruthTable(sample_outputs)
    print(tt.get_truth_table())