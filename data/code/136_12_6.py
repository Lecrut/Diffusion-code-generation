class LogicalOperations:
    def apply_operators(self, expressions):
        results = []
        for expr in expressions:
            result = expr
            for op in ['and', 'or', 'not']:
                if op == 'and':
                    result = result and expr[1] if len(expr) > 1 else False
                elif op == 'or':
                    result = result or expr[1] if len(expr) > 1 else False
                elif op == 'not':
                    result = not result
            results.append(result)
        return results
if __name__ == '__main__':
    lo = LogicalOperations()
    sample_expressions = [
        (True, True, False),
        (False, True, True),
        (True, False, False)
    ]
    results = lo.apply_operators(sample_expressions)
    print(results)