class LogicEvaluator:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def evaluate_expression(self):
        return (self.a and self.b) or (self.c and not self.d)

if __name__ == '__main__':
    evaluator = LogicEvaluator(1, 0, 1, 0)
    result = evaluator.evaluate_expression()
    print(result)