class TruthTable:
    def __init__(self, outputs):
        self.outputs = outputs
        self.table = []

    def generate_table(self):
        num_vars = len(bin(len(self.outputs) - 1)[2:])
        for i in range(2 ** num_vars):
            binary = bin(i)[2:].zfill(num_vars)
            inputs = tuple(int(bit) for bit in binary)
            self.table.append((inputs, self.outputs[i]))

    def get_table(self):
        return self.table

if __name__ == '__main__':
    outputs = [0, 1, 1, 0]
    tt = TruthTable(outputs)
    tt.generate_table()
    print(tt.get_table())