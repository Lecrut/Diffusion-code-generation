class TruthTable:
    def __init__(self, outputs):
        self.outputs = outputs
        self.table = [0] * (2 ** len(outputs))

    def compute(self):
        for i in range(len(self.table)):
            index = 0
            bit_position = 0
            while i > 0:
                if i & 1:
                    index |= (1 << bit_position)
                bit_position += 1
                i >>= 1
            self.table[index] = self.outputs[i]

    def get_table(self):
        return self.table

if __name__ == '__main__':
    tt = TruthTable([0, 1, 1, 0])
    tt.compute()
    print(tt.get_table())