class TruthTableGenerator:
    def generate_truth_table(self, n):
        num_rows = 2**n
        truth_table = [[(i >> j) & 1 for j in range(n)] for i in range(num_rows)]
        return truth_table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    truth_table_data = generator.generate_truth_table(3)
    for row in truth_table_data:
        print(" ".join(map(str, row)))