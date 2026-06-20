class LogicEvaluator:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def evaluate_expression(self):
        return (self.A & self.B) | (self.C & ~self.D)

if __name__ == '__main__':
    evaluator = LogicEvaluator(1, 0, 1, 0)
    result = evaluator.evaluate_expression()
    print(result)