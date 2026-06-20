class BooleanListChecker:
    @staticmethod
    def check_any_true(boolean_list):
        return any(boolean_list)

if __name__ == '__main__':
    list1 = [False, False, False, True, False]
    list2 = [False, False, False]
    list3 = [True, True, True]
    list4 = []
    list5 = [False]
    print(f"List 1: {BooleanListChecker.check_any_true(list1)}")
    print(f"List 2: {BooleanListChecker.check_any_true(list2)}")
    print(f"List 3: {BooleanListChecker.check_any_true(list3)}")
    print(f"List 4: {BooleanListChecker.check_any_true(list4)}")
    print(f"List 5: {BooleanListChecker.check_any_true(list5)}")