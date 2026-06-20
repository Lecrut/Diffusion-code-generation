class BooleanChecker:
    def has_at_least_one_true(self, boolean_list):
        return any(boolean_list)

if __name__ == '__main__':
    checker = BooleanChecker()
    list1 = [False, False, True]
    list2 = [False, False, False]
    list3 = []
    print(f"List 1: {list1}, Result: {checker.has_at_least_one_true(list1)}")
    print(f"List 2: {list2}, Result: {checker.has_at_least_one_true(list2)}")
    print(f"List 3: {list3}, Result: {checker.has_at_least_one_true(list3)}")