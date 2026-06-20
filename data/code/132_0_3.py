class LogicEvaluator:
    @staticmethod
    def evaluate_logic(a, b):
        return a & b

if __name__ == '__main__':
    print(LogicEvaluator.evaluate_logic(True, False))