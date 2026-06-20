class ExpressionEvaluator:
    @staticmethod
    def evaluate(X, Y, Z, W):
        return (X and Y) or (Z and not W)

if __name__ == '__main__':
    result = ExpressionEvaluator.evaluate(True, False, True, False)
    print(result)