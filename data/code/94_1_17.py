class BooleanChecker:
    @staticmethod
    def check_any_true(iterable):
        return any(iterable)

if __name__ == '__main__':
    checker = BooleanChecker()
    print(f"list1: {checker.check_any_true([False, False, True, False])}")
    print(f"list2: {checker.check_any_true((False, False, False))}")