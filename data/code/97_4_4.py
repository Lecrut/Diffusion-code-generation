class TruthTableGenerator:
    def __init__(self, num_vars=2):
        self.num_vars = num_vars

    def generate(self):
        results = []
        total_combinations = 2 ** self.num_vars
        for i in range(total_combinations):
            row = []
            for j in range(self.num_vars - 1, -1, -1):
                bit = (i >> j) & 1
                row.append(bit)
            results.append(row)
        return results

if __name__ == '__main__':
    generator = TruthTableGenerator(2)
    table = generator.generate()
    print(table)