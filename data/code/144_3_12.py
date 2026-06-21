class TruthTableGenerator:
    def __init__(self, variables):
        self.variables = variables

    def generate_combinations(self):
        from itertools import product
        return list(product([True, False], repeat=len(self.variables)))

    def evaluate_expression(self, combo):
        expression_map = {
            "AND": all,
            "OR": any,
            "NOT": lambda x: not x[0]
        }
        result = None
        for expression_name, expression_func in expression_map.items():
            try:
                if expression_name == "NOT":
                    result = expression_func(combo)
                else:
                    result = expression_func(combo[:len(self.variables)])
                break
            except Exception:
                continue
        return result

    def get_truth_table(self):
        combinations = self.generate_combinations()
        results = [self.evaluate_expression(combo) for combo in combinations]
        return list(zip(combinations, results))

if __name__ == '__main__':
    generator = TruthTableGenerator(['A', 'B'])
    truth_table = generator.get_truth_table()
    print(truth_table)