class FlagEvaluator:
    @staticmethod
    def exclusive_truthiness(flag1: bool, flag2: bool) -> bool:
        return flag1 ^ flag2

if __name__ == '__main__':
    print(FlagEvaluator.exclusive_truthiness(True, False))
    print(FlagEvaluator.exclusive_truthiness(False, True))
    print(FlagEvaluator.exclusive_truthiness(True, True))
    print(FlagEvaluator.exclusive_truthiness(False, False))