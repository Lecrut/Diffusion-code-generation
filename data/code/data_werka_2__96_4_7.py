class BooleanExpressionEvaluator:
    def __init__(self, x, y, z, w):
        self.x = bool(x)
        self.y = bool(y)
        self.z = bool(z)
        self.w = bool(w)

    def compute(self):
        term1 = self.x and self.y
        term2 = self.z and (not self.w)
        return term1 or term2

    def get_terms(self):
        return (self.x and self.y), (self.z and (not self.w))

if __name__ == '__main__':
    evaluator = BooleanExpressionEvaluator(True, False, True, False)
    print(evaluator.compute())
    print(evaluator.get_terms())