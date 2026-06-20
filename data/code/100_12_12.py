class LogicalEvaluator:
    def __init__(self):
        self.values = {}

    def set_value(self, var, value):
        self.values[var] = value

    def evaluate(self, statement):
        parts = statement.split()
        if len(parts) != 3 or parts[1] not in ['AND', 'OR']:
            raise ValueError("Invalid statement format")
        return eval(f"{self.values[parts[0]]} {parts[1]} {self.values[parts[2]]}")

if __name__ == '__main__':
    evaluator = LogicalEvaluator()
    evaluator.set_value('A', True)
    evaluator.set_value('B', False)
    print(f"A AND B: {evaluator.evaluate('A AND B')}")
    print(f"A OR B: {evaluator.evaluate('A OR B')}")