class BooleanChecker:
    FALSE_STATE = False

    @staticmethod
    def is_false(value: bool) -> bool:
        return value is BooleanChecker.FALSE_STATE

    @staticmethod
    def both_false(val_a: bool, val_b: bool) -> bool:
        return BooleanChecker.is_false(val_a) and BooleanChecker.is_false(val_b)

if __name__ == '__main__':
    a = False
    b = False
    result = BooleanChecker.both_false(a, b)
    print(result)