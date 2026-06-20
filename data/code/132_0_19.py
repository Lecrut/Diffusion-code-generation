class LogicEvaluator:
    @staticmethod
    def evaluate_logic(a: bool, b: bool) -> bool:
        return a & b

if __name__ == '__main__':
    result = LogicEvaluator.evaluate_logic(True, False)
    print(result)