class BooleanEvaluator:
    def __init__(self, input_a, input_b):
        self.a = input_a
        self.b = input_b

    def check_both_false(self):
        return self.a is False and self.b is False

    def evaluate(self):
        return not (self.a or self.b)

if __name__ == '__main__':
    evaluator1 = BooleanEvaluator(False, False)
    print(evaluator1.check_both_false())
    print(evaluator1.evaluate())
    
    evaluator2 = BooleanEvaluator(True, False)
    print(evaluator2.check_both_false())
    print(evaluator2.evaluate())