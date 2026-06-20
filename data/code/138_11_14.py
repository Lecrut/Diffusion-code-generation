class TruthTable:
    def __init__(self, outputs):
        self.outputs = outputs

    def get_truth_table(self):
        n = len(self.outputs)
        num_inputs = n.bit_length() - 1
        truth_table = []
        for i in range(2**num_inputs):
            binary = format(i, f'0{num_inputs}b')
            inputs = tuple(int(bit) for bit in binary)
            output = self.outputs[i]
            truth_table.append((inputs, output))
        return truth_table

if __name__ == '__main__':
    outputs = [1, 0, 1, 0]
    tt = TruthTable(outputs)
    print(tt.get_truth_table())