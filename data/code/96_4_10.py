class BooleanEvaluator:
    def evaluate(self, X, Y, Z, W):
        return (X and Y) or (Z and not W)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result = evaluator.evaluate(True, False, True, False)
    print(result)