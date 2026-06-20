class LogicEvaluator:
    A = 1
    B = 0
    C = 1
    D = 0

    @staticmethod
    def evaluate_expression():
        result = (LogicEvaluator.A & LogicEvaluator.B) | (LogicEvaluator.C & ~LogicEvaluator.D)
        return result

if __name__ == '__main__':
    evaluator = LogicEvaluator()
    print(evaluator.evaluate_expression())