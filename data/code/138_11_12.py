class TruthTable:
    def __init__(self, outputs):
        self.outputs = outputs
        self.table = []

    def generate_table(self):
        num_inputs = len(bin(len(self.outputs) - 1)[2:])
        for i in range(2 ** num_inputs):
            input_bits = bin(i)[2:].zfill(num_inputs)
            output_index = int(input_bits, 2)
            self.table.append((input_bits, self.outputs[output_index]))

    def get_table(self):
        return self.table

if __name__ == '__main__':
    sample_outputs = [0, 1, 1, 0]
    tt = TruthTable(sample_outputs)
    tt.generate_table()
    print(tt.get_table())