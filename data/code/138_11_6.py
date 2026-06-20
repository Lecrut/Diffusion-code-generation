class TruthTable:
    def __init__(self, outputs):
        self.outputs = outputs

    def get_truth_table(self):
        num_inputs = len(bin(len(self.outputs) - 1)[2:])
        table = []
        for i in range(2 ** num_inputs):
            inputs = [bool((i >> j) & 1) for j in range(num_inputs)]
            output = self.outputs[i]
            table.append((*inputs, output))
        return table

if __name__ == '__main__':
    tt = TruthTable([0, 1, 1, 0])
    print(tt.get_truth_table())