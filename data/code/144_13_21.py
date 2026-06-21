class ExpressionEvaluator:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self, assignment):
        P = assignment[0]
        Q = assignment[1]
        try:
            return eval(self.expression, {"__builtins__": None}, {"P": P, "Q": Q})
        except Exception:
            return False

if __name__ == '__main__':
    evaluator = ExpressionEvaluator("P and Q or not P")
    input_assignments = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    results = {assignment: evaluator.evaluate(assignment) for assignment in input_assignments}
    print(results)