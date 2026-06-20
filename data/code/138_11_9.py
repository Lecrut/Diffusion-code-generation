class TruthTable:
    def __init__(self, outputs):
        self.outputs = outputs
        self.table = self._generate_table()

    def _generate_table(self):
        n = len(self.outputs)
        table_size = 2 ** n
        return [self.outputs[i // (table_size // 2)] for i in range(table_size)]

    def get_output(self, inputs):
        index = sum(1 << i if inputs[i] else 0 for i in range(len(inputs)))
        return self.table[index]

if __name__ == '__main__':
    tt = TruthTable([False, True, False, True])
    print(tt.get_output([True, False]))