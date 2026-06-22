class LogicEvaluator:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def evaluate_nested_logic(self):
        first_term = self.a and self.b
        second_term = self.c and (not self.d)
        return first_term or second_term

if __name__ == '__main__':
    evaluator = LogicEvaluator(True, False, True, False)
    print(evaluator.evaluate_nested_logic())
    evaluator2 = LogicEvaluator(False, True, False, True)
    print(evaluator2.evaluate_nested_logic())
    evaluator3 = LogicEvaluator(True, True, False, True)
    print(evaluator3.evaluate_nested_logic())
    evaluator4 = LogicEvaluator(False, False, True, False)
    print(evaluator4.evaluate_nested_logic())