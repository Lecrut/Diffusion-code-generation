class StatementEvaluator:
    def __init__(self):
        self.statements = ["True", "False", "2 + 2 == 4", "3 > 5"]

    def evaluate_statements(self):
        results = []
        for statement in self.statements:
            try:
                result = eval(statement)
                results.append((statement, result))
            except Exception as e:
                results.append((statement, f"Error: {str(e)}"))
        return results

if __name__ == '__main__':
    evaluator = StatementEvaluator()
    results = evaluator.evaluate_statements()
    for statement, result in results:
        print(f"{statement}: {result}")