class BooleanChecker:
    @staticmethod
    def check_any_true(boolean_list):
        return any(boolean_list)

if __name__ == '__main__':
    list1 = [False, False, False, True, False]
    list2 = [False, False, False]
    list3 = [True, True, True]
    list4 = []
    list5 = [False]
    
    checker = BooleanChecker()
    print(f"List 1: {checker.check_any_true(list1)}")
    print(f"List 2: {checker.check_any_true(list2)}")
    print(f"List 3: {checker.check_any_true(list3)}")
    print(f"List 4: {checker.check_any_true(list4)}")
    print(f"List 5: {checker.check_any_true(list5)}")