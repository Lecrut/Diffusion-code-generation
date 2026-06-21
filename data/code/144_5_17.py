class TruthTableGenerator:
    NUM_VARIABLES = 3

    @staticmethod
    def generate_truth_table():
        num_rows = 2 ** TruthTableGenerator.NUM_VARIABLES
        truth_table = []
        for i in range(num_rows):
            row = []
            for j in range(TruthTableGenerator.NUM_VARIABLES):
                bit = (i >> j) & 1
                row.append(bit)
            truth_table.append(row)
        return truth_table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    result = generator.generate_truth_table()
    print(result)