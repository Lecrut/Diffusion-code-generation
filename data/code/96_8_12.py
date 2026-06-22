class LogicEvaluator:
    def __init__(self, a, b, c, d):
        self.a = bool(a)
        self.b = bool(b)
        self.c = bool(c)
        self.d = bool(d)

    def evaluate(self):
        left_side = self.a and self.b
        right_side = self.c and (not self.d)
        return left_side or right_side

if __name__ == '__main__':
    evaluator = LogicEvaluator(False, True, True, False)
    print(evaluator.evaluate())