class NumberEvaluator:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_conditions(self):
        return self.a > 0 and self.b < self.a and self.c == self.a + self.b

if __name__ == '__main__':
    evaluator = NumberEvaluator(5, 3, 8)
    print(evaluator.check_conditions())