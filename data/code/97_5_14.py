class TruthTableGenerator:
    NUM_INPUTS = 4

    def generate_truth_table(self):
        table = []
        for i in range(2 ** self.NUM_INPUTS):
            row = [bool(i & (1 << j)) for j in range(self.NUM_INPUTS)]
            table.append(row)
        return table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    truth_table = generator.generate_truth_table()
    for row in truth_table:
        print(row)