class LogicEvaluator:
    def verify_status(self, a: bool, b: bool) -> bool:
        return a ^ b

if __name__ == '__main__':
    evaluator = LogicEvaluator()
    print(evaluator.verify_status(True, False))
    print(evaluator.verify_status(False, True))
    print(evaluator.verify_status(True, True))
    print(evaluator.verify_status(False, False))