class ExpressionEvaluator:
    def evaluate_expressions(self):
        results = []
        for A in [False, True]:
            for B in [False, True]:
                expr1 = (A ^ B)
                expr2 = (not A) and B
                results.append((A, B, expr1 == expr2))
        return results

if __name__ == '__main__':
    evaluator = ExpressionEvaluator()
    evaluation_results = evaluator.evaluate_expressions()
    for result in evaluation_results:
        print(result)