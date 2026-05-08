class LogicalOperations:
    def apply_operators(self, expressions):
        results = []
        for expr in expressions:
            results.append(expr)
        return results
if __name__ == '__main__':
    lo = LogicalOperations()
    expressions1 = [True, False, True]
    results1 = lo.apply_operators(expressions1)
    print(results1)
    expressions2 = [True, True, False]
    results2 = lo.apply_operators(expressions2)
    print(results2)
    expressions3 = [True, False, False, True]
    results3 = lo.apply_operators(expressions3)
    print(results3)