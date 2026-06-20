class TruthTable:
    def __init__(self, outputs):
        self.outputs = outputs
        self.table = []

    def compute_table(self):
        n = len(self.outputs)
        for i in range(1 << n):
            row = []
            for j in range(n):
                row.append((i >> j) & 1)
            row.append(self.outputs[i])
            self.table.append(row)

    def get_table(self):
        return self.table

if __name__ == '__main__':
    outputs = [0, 1, 1, 0]
    tt = TruthTable(outputs)
    tt.compute_table()
    print(tt.get_table())