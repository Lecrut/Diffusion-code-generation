class LogicEvaluator:
    TRUE = True
    FALSE = False
    
    @staticmethod
    def check_both_true(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    print(LogicEvaluator.check_both_true(True, True))
    print(LogicEvaluator.check_both_true(False, True))
    print(LogicEvaluator.check_both_true(True, False))
    print(LogicEvaluator.check_both_true(False, False))