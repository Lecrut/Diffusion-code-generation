class BooleanChecker:
    def has_at_least_one_true(self, boolean_list):
        if not isinstance(boolean_list, list) or not all(isinstance(x, bool) for x in boolean_list):
            raise ValueError("Input must be a list of booleans")
        return any(boolean_list)

if __name__ == '__main__':
    checker = BooleanChecker()
    list1 = [False, False, False]
    list2 = [False, True, False]
    list3 = [True, True, False]
    list4 = []
    list5 = [False]
    print(f"List 1 has at least one true: {checker.has_at_least_one_true(list1)}")
    print(f"List 2 has at least one true: {checker.has_at_least_one_true(list2)}")
    print(f"List 3 has at least one true: {checker.has_at_least_one_true(list3)}")
    print(f"List 4 has at least one true: {checker.has_at_least_one_true(list4)}")
    print(f"List 5 has at least one true: {checker.has_at_least_one_true(list5)}")