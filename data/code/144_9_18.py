class TruthTableGenerator:
    def __init__(self, n):
        self.n = n

    def generate_truth_table(self):
        num_rows = 2**self.n
        return [
            [(i >> j) & 1 for j in range(self.n)]
            for i in range(num_rows)
        ]

if __name__ == '__main__':
    generator = TruthTableGenerator(3)
    truth_table_data = generator.generate_truth_table()
    for row in truth_table_data:
        print(" ".join(str(bit) for bit in row))