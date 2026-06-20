class RelationalEvaluator:
    def __init__(self):
        self.expressions = [
            '1 > 0',
            '2 < 3',
            '4 == 4',
            '5 != 6'
        ]

    def evaluate_expressions(self):
        results = []
        for expr in self.expressions:
            try:
                result = eval(expr)
                results.append(result)
            except Exception as e:
                results.append(str(e))
        return results

if __name__ == '__main__':
    evaluator = RelationalEvaluator()
    results = evaluator.evaluate_expressions()
    print(results)