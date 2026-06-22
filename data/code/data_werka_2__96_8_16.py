class LogicEvaluator:
    def __init__(self, a, b, c, d):
        self.a = bool(a)
        self.b = bool(b)
        self.c = bool(c)
        self.d = bool(d)

    def evaluate(self):
        return (self.a and self.b) or (self.c and not self.d)

    def first_part(self):
        return self.a and self.b

    def second_part(self):
        return self.c and not self.d

if __name__ == '__main__':
    evaluator = LogicEvaluator(False, True, True, True)
    print(evaluator.first_part())
    print(evaluator.second_part())
    print(evaluator.evaluate())