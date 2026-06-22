class TruthTableGenerator:
    def __init__(self, num_vars=3):
        if num_vars < 1:
            raise ValueError("Number of variables must be at least 1")
        self.num_vars = num_vars
        self.var_names = [chr(ord('A') + i) for i in range(num_vars)]

    def generate(self):
        rows = []
        total_combinations = 2 ** self.num_vars
        for i in range(total_combinations):
            row = {}
            for j in range(self.num_vars):
                bit = (i >> (self.num_vars - 1 - j)) & 1
                row[self.var_names[j]] = bool(bit)
            rows.append(row)
        return rows

    def display(self, rows):
        header = " | ".join(self.var_names)
        print(header)
        print("-" * len(header))
        for row in rows:
            values = [str(int(row[var])) for var in self.var_names]
            print(" | ".join(values))

if __name__ == '__main__':
    generator = TruthTableGenerator(3)
    table = generator.generate()
    generator.display(table)
    print(table[0])