class TruthTableGenerator:
    def __init__(self, num_vars=3):
        if num_vars < 1 or num_vars > 10:
            raise ValueError("Number of variables must be between 1 and 10")
        self.num_vars = num_vars
        self.var_names = [chr(ord('A') + i) for i in range(num_vars)]
        self.rows = 2 ** num_vars

    def _get_combinations(self):
        combinations = []
        for i in range(self.rows):
            row = []
            for j in range(self.num_vars - 1, -1, -1):
                bit = (i >> j) & 1
                row.append(bool(bit))
            combinations.append(row)
        return combinations

    def generate(self):
        combinations = self._get_combinations()
        header = " | ".join(self.var_names)
        print(header)
        print("-" * len(header))
        for combo in combinations:
            row_str = " | ".join(str(int(val)) for val in combo)
            print(row_str)
        return combinations

    def evaluate_expression(self, expression_func):
        combinations = self._get_combinations()
        results = []
        for combo in combinations:
            result = expression_func(*combo)
            results.append(result)
        return results

if __name__ == '__main__':
    generator = TruthTableGenerator(3)
    generator.generate()
    
    def and_expr(a, b, c):
        return a and b and c
    
    results = generator.evaluate_expression(and_expr)
    print(results)