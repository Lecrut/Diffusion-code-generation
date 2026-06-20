class LogicEvaluator:
    @staticmethod
    def verify_status(a: bool, b: bool) -> bool:
        return a ^ b

if __name__ == '__main__':
    print(LogicEvaluator.verify_status(True, False))
    print(LogicEvaluator.verify_status(False, True))
    print(LogicEvaluator.verify_status(True, True))
    print(LogicEvaluator.verify_status(False, False))