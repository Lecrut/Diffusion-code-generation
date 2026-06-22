class BooleanEvaluator:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def evaluate(self):
        term_one = self.a and self.b
        term_two = self.c and not self.d
        return term_one or term_two

if __name__ == '__main__':
    evaluator = BooleanEvaluator(a=True, b=False, c=True, d=False)
    print(evaluator.evaluate())
    print(not evaluator.evaluate())