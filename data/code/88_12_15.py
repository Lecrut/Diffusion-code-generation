class BooleanConjunction:
    @staticmethod
    def check_both_true(a: bool, b: bool) -> bool:
        return a & b

if __name__ == '__main__':
    print(BooleanConjunction.check_both_true(True, True))
    print(BooleanConjunction.check_both_true(False, True))
    print(BooleanConjunction.check_both_true(True, False))
    print(BooleanConjunction.check_both_true(False, False))