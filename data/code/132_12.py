class BooleanHandler:
    def evaluate(self, bool_list: list[bool]) -> bool:
        if not bool_list:
            return True
        result = True
        for value in bool_list:
            result = result and value
        return result
if __name__ == '__main__':
    handler = BooleanHandler()
    list1 = [True, True, False]
    list2 = [True, True, True]
    list3 = [False, False]
    list4 = []
    list5 = [True]
    print(f"Evaluating {list1}: {handler.evaluate(list1)}")
    print(f"Evaluating {list2}: {handler.evaluate(list2)}")
    print(f"Evaluating {list3}: {handler.evaluate(list3)}")
    print(f"Evaluating {list4}: {handler.evaluate(list4)}")
    print(f"Evaluating {list5}: {handler.evaluate(list5)}")