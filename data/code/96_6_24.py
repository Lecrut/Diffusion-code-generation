class LogicEvaluator:
    def evaluate(self, A, B, C, D):
        return (A & B) | (C & ~D)

if __name__ == '__main__':
    evaluator = LogicEvaluator()
    result = evaluator.evaluate(1, 0, 1, 0)
    print(result)