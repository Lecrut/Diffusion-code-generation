class LogicalOperations:
    def apply_operators(self, expressions):
        results = []
        for expr in expressions:
            try:
                result = eval(f"({expr})")
                results.append(result)
            except Exception:
                results.append(None)
        return results
if __name__ == '__main__':
    logic_ops = LogicalOperations()
    sample_expressions = [
        "True and False",
        "True or False",
        "not True",
        "False and False",
        "True or True"
    ]
    results = logic_ops.apply_operators(sample_expressions)
    print(results)