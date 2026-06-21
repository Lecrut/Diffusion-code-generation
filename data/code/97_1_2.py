class TruthTableGenerator:
    def __init__(self, num_vars=3):
        self.num_vars = num_vars
        self.var_names = ['A', 'B', 'C', 'D', 'E', 'F'][:num_vars]

    def generate(self):
        rows = []
        total_combinations = 2 ** self.num_vars
        for i in range(total_combinations):
            row = []
            for j in range(self.num_vars - 1, -1, -1):
                bit = (i >> j) & 1
                row.append(bit)
            rows.append(row)
        return rows

    def display(self, rows):
        header = ' | '.join(self.var_names)
        print(header)
        print('-' * len(header))
        for row in rows:
            print(' | '.join(str(val) for val in row))

if __name__ == '__main__':
    generator = TruthTableGenerator(3)
    rows = generator.generate()
    generator.display(rows)
    print(rows)