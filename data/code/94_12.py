class BooleanChecker:
    def has_at_least_one_true(self, boolean_list):
        for boolean in boolean_list:
            if boolean:
                return True
        return False
if __name__ == '__main__':
    checker = BooleanChecker()
    list1 = [False, False, False]
    list2 = [False, True, False]
    list3 = [True, True, False]
    list4 = []
    list5 = [False]
    print(f"List 1: {list1}, Result: {checker.has_at_least_one_true(list1)}")
    print(f"List 2: {list2}, Result: {checker.has_at_least_one_true(list2)}")
    print(f"List 3: {list3}, Result: {checker.has_at_least_one_true(list3)}")
    print(f"List 4: {list4}, Result: {checker.has_at_least_one_true(list4)}")
    print(f"List 5: {list5}, Result: {checker.has_at_least_one_true(list5)}")