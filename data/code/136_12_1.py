class LogicalOperations:
    def apply_operators(self, expressions):
        results = []
        for expr in expressions:
            results.append(expr)
        return results
if __name__ == '__main__':
    logic_ops = LogicalOperations()
    expressions = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    results = logic_ops.apply_operators(expressions)
    print(results)