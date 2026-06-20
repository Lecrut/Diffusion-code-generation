class BoolChecker:
    @staticmethod
    def both_false(a: bool, b: bool) -> bool:
        return not a and not b

if __name__ == '__main__':
    result = BoolChecker.both_false(False, False)
    print(result)