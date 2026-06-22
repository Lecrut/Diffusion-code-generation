class BooleanExpressionEvaluator:
    EXPRESSION_STR = "(X and Y) or (Z and not W)"

    def __init__(self, X, Y, Z, W):
        self.X = bool(X)
        self.Y = bool(Y)
        self.Z = bool(Z)
        self.W = bool(W)

    @staticmethod
    def get_expression_template():
        return BooleanExpressionEvaluator.EXPRESSION_STR

    def evaluate(self):
        term1 = self.X and self.Y
        term2 = self.Z and (not self.W)
        return term1 or term2

if __name__ == '__main__':
    evaluator = BooleanExpressionEvaluator(0, 1, 0, 1)
    result = evaluator.evaluate()
    print(result)