class BoolChecker:
    @staticmethod
    def check_any_true(iterable):
        return any(iterable)

if __name__ == '__main__':
    checker = BoolChecker()
    print(f"list1: {checker.check_any_true([False, False, True, False])}")
    print(f"list2: {checker.check_any_true([False, False, False])}")
    print(f"list3: {checker.check_any_true([True])}")
    print(f"list4: {checker.check_any_true([])}")
    print(f"list5: {checker.check_any_true([False, False, False, False])}")