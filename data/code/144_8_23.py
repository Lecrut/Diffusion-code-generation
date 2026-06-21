class TruthTableEvaluator:
    def __init__(self):
        self.combinations = list(itertools.product([0, 1], repeat=4))

    def evaluate_expression(self, combination):
        A, B, C, D = combination
        return (A or B) and (C or D)

    def generate_truth_table(self):
        results = []
        for combo in self.combinations:
            result = self.evaluate_expression(combo)
            results.append((combo, result))
        return results

if __name__ == '__main__':
    evaluator = TruthTableEvaluator()
    truth_table = evaluator.generate_truth_table()
    print(truth_table)