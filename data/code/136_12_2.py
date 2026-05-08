class LogicalOperations:
    def apply_operators(self, expressions):
        results = []
        for expr in expressions:
            if isinstance(expr, list):
                result = expr[0]
                for i in range(1, len(expr)):
                    result = result and expr[i]
                results.append(result)
            else:
                results.append(expr)
        return results
if __name__ == '__main__':
    lo = LogicalOperations()
    sample_expressions = [
        [True, True, False],
        [False, True],
        [True, True, True, False],
        [False]
    ]
    results = lo.apply_operators(sample_expressions)
    print(results)