class TruthTable:
    def __init__(self, outputs):
        self.outputs = outputs
        self.table = {}

    def compute_table(self):
        n = len(self.outputs)
        for i in range(2**n):
            inputs = [bool((i >> j) & 1) for j in range(n)]
            self.table[tuple(inputs)] = self.outputs[i]

    def get_output(self, inputs):
        return self.table.get(tuple(inputs), None)

if __name__ == '__main__':
    outputs = [0, 1, 1, 0]
    tt = TruthTable(outputs)
    tt.compute_table()
    print(tt.get_output([True, False]))