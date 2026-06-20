class BooleanChecker:
    @staticmethod
    def check_any_true(iterable):
        return any(iterable)

if __name__ == '__main__':
    checker = BooleanChecker()
    list1 = [False, False, True, False]
    list2 = [False, False, False]
    list3 = [True]
    list4 = []
    print(f"list1: {checker.check_any_true(list1)}")
    print(f"list2: {checker.check_any_true(list2)}")
    print(f"list3: {checker.check_any_true(list3)}")
    print(f"list4: {checker.check_any_true(list4)}")