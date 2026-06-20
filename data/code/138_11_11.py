class TruthTable:
    def __init__(self, outputs):
        self.outputs = outputs
        self.table = [0] * (2 ** len(outputs))

    def compute(self):
        for i in range(len(self.table)):
            index = 0
            for j in range(len(self.outputs)):
                if i & (1 << j):
                    index |= (1 << j)
            self.table[i] = self.outputs[index]

if __name__ == '__main__':
    tt = TruthTable([0, 1, 1, 0])
    tt.compute()
    print(tt.table)