class BoolChecker:
    @staticmethod
    def check_both_false(a: bool, b: bool) -> bool:
        return not a and not b

if __name__ == '__main__':
    result = BoolChecker.check_both_false(False, False)
    print(result)