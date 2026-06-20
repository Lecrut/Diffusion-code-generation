class LogicEvaluator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def evaluate_or(self):
        return bool(self.a or self.b)
if __name__ == '__main__':
    evaluator1 = LogicEvaluator(True, False)
    print(evaluator1.evaluate_or())
    evaluator2 = LogicEvaluator(False, True)
    print(evaluator2.evaluate_or())
    evaluator3 = LogicEvaluator(False, False)
    print(evaluator3.evaluate_or())