class BooleanFlagEvaluator:
    @staticmethod
    def exclusive_truthiness(flag1: bool, flag2: bool) -> bool:
        return flag1 ^ flag2

if __name__ == '__main__':
    print(BooleanFlagEvaluator.exclusive_truthiness(True, False))
    print(BooleanFlagEvaluator.exclusive_truthiness(False, True))
    print(BooleanFlagEvaluator.exclusive_truthiness(True, True))
    print(BooleanFlagEvaluator.exclusive_truthiness(False, False))