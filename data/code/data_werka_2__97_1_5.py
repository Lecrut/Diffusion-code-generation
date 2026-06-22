class TruthTableGenerator:
    def __init__(self, num_vars=3):
        if num_vars < 1 or num_vars > 10:
            raise ValueError("Invalid number of variables")
        self.num_vars = num_vars
        self.var_names = [chr(ord('A') + i) for i in range(num_vars)]

    def _get_combinations(self):
        combinations = []
        for i in range(2 ** self.num_vars):
            row = []
            for j in range(self.num_vars - 1, -1, -1):
                bit = (i >> j) & 1
                row.append(bool(bit))
            combinations.append(row)
        return combinations

    def generate(self):
        combinations = self._get_combinations()
        header = ' | '.join(self.var_names)
        result = [header]
        result.append('-' * len(header))
        for combo in combinations:
            row_str = ' | '.join(str(int(val)) for val in combo)
            result.append(row_str)
        return '\n'.join(result)

if __name__ == '__main__':
    generator = TruthTableGenerator(3)
    print(generator.generate())