class LogicalConsistencyChecker:
    def __init__(self):
        self.logical_operators = {
            "AND": lambda x, y: x and y,
            "OR": lambda x, y: x or y,
            "NOT": lambda x: not x
        }

    def evaluate_expression(self, expr: str) -> bool:
        return eval(expr)

    def check_pairwise_consistency(self, pairs):
        for pair in pairs:
            expr1, expr2 = pair
            value1 = self.evaluate_expression(expr1)
            value2 = self.evaluate_expression(expr2)
            if not (self.logical_operators.get("AND", lambda x, y: False)(value1, value2) or
                    self.logical_operators.get("OR", lambda x, y: False)(value1, value2)):
                return False
        return True

if __name__ == '__main__':
    checker = LogicalConsistencyChecker()
    pairs = [
        ("True and False", "False or True"),
        ("A and not A", "B and not B")
    ]
    result = checker.check_pairwise_consistency(pairs)
    print(result)