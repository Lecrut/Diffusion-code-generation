class LogicChecker:
    def evaluate(self, bool_list):
        for value in bool_list:
            if not value:
                return False
        return True
if __name__ == '__main__':
    checker = LogicChecker()
    list1 = [True, True, True]
    list2 = [True, False, True]
    list3 = [True, True, False]
    list4 = []
    list5 = [True]
    print(f"List 1: {checker.evaluate(list1)}")
    print(f"List 2: {checker.evaluate(list2)}")
    print(f"List 3: {checker.evaluate(list3)}")
    print(f"List 4: {checker.evaluate(list4)}")
    print(f"List 5: {checker.evaluate(list5)}")