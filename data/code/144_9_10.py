class TruthTableGenerator:
    def __init__(self, n):
        self.n = n
        self.truth_table = []

    def generate_truth_table(self):
        num_rows = 2**self.n
        for i in range(num_rows):
            binary_representation = format(i, f'0{self.n}b')
            row = [int(bit) for bit in binary_representation]
            self.truth_table.append(row)
        return self.truth_table

if __name__ == '__main__':
    generator = TruthTableGenerator(3)
    table = generator.generate_truth_table()
    for row in table:
        print(" ".join(map(str, row)))