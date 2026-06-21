class TruthTableEvaluator:
    def __init__(self):
        self.var_names = ['A', 'B', 'C']

    def evaluate_expression(self, expression, var1, var2, var3):
        if "AND" in expression:
            return var1 and var2
        elif "OR" in expression:
            return var1 or var2
        elif "NOT" in expression:
            if expression == "NOT C":
                return not var3
            else:
                raise ValueError("Invalid NOT operation")
        else:
            raise ValueError("Unsupported operation")

    def generate_truth_table(self):
        results = []
        for a in [False, True]:
            for b in [False, True]:
                for c in [False, True]:
                    result = self.evaluate_expression("(A AND B) OR (NOT C)", a, b, c)
                    results.append({'A': a, 'B': b, 'C': c, 'Result': result})
        return results

if __name__ == '__main__':
    evaluator = TruthTableEvaluator()
    truth_table = evaluator.generate_truth_table()
    for row in truth_table:
        print(row)