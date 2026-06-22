def check_equality(item1, item2):
    if item1 is item2:
        return True
    if type(item1) != type(item2):
        return False
    if isinstance(item1, (int, float, str, tuple)):
        return item1 == item2
    if isinstance(item1, list):
        if len(item1) != len(item2):
            return False
        for sub_item1, sub_item2 in zip(item1, item2):
            if not check_equality(sub_item1, sub_item2):
                return False
        return True
    if isinstance(item1, dict):
        if len(item1) != len(item2):
            return False
        for key in item1:
            if key not in item2 or not check_equality(item1[key], item2[key]):
                return False
        return True
    if isinstance(item1, set):
        if len(item1) != len(item2):
            return False
        for sub_item in item1:
            if sub_item not in item2:
                return False
        return True
    return item1 == item2
if __name__ == '__main__':
    print(check_equality([1, 2, [3, 4]], [1, 2, [3, 4]]))
    print(check_equality({'a': 1, 'b': 2}, {'a': 1, 'b': 2}))
    print(check_equality({1, 2, 3}, {1, 2, 3}))
    print(check_equality((1, 2), (1, 2)))
    print(check_equality(1.0, 1))
    print(check_equality('hello', 'world'))