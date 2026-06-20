class TruthTable:
    def __init__(self, outputs):
        self.outputs = outputs
        self.num_vars = len(outputs) ** 0.5
        if not self.num_vars.is_integer():
            raise ValueError("Output list length must be a perfect square")
        self.num_vars = int(self.num_vars)

    def get_truth_table(self):
        truth_table = []
        for i in range(2 ** self.num_vars):
            inputs = [bool((i >> j) & 1) for j in range(self.num_vars)]
            output_index = sum(inputs[::-1])
            truth_table.append((inputs, self.outputs[output_index]))
        return truth_table

if __name__ == '__main__':
    outputs = [False, True, False, True]
    tt = TruthTable(outputs)
    print(tt.get_truth_table())