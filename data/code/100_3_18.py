class LogicChecker:
    def evaluate(self, bool_list):
        return all(bool_list)

if __name__ == '__main__':
    checker = LogicChecker()
    list1 = [True, True, True]
    list2 = [True, False, True]
    list3 = [True, True, False]
    list4 = []
    list5 = [True]
    print(f"List 1: {list1}, Result: {checker.evaluate(list1)}")
    print(f"List 2: {list2}, Result: {checker.evaluate(list2)}")
    print(f"List 3: {list3}, Result: {checker.evaluate(list3)}")
    print(f"List 4: {list4}, Result: {checker.evaluate(list4)}")
    print(f"List 5: {list5}, Result: {checker.evaluate(list5)}")