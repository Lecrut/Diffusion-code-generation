class LogicEvaluator:
    @staticmethod
    def xor(a: bool, b: bool) -> bool:
        return a ^ b

if __name__ == '__main__':
    print(LogicEvaluator.xor(True, False))
    print(LogicEvaluator.xor(False, True))
    print(LogicEvaluator.xor(True, True))
    print(LogicEvaluator.xor(False, False))