class BooleanChecker:
    @staticmethod
    def is_both_false(a: bool, b: bool) -> bool:
        return not a and not b

if __name__ == '__main__':
    print(BooleanChecker.is_both_false(False, False))