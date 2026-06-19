def check_equality(item1, item2):
    if id(item1) == id(item2):
        return True
    if type(item1) != type(item2):
        return False
    if isinstance(item1, (int, float, str, bool)):
        return item1 == item2
    if isinstance(item1, list):
        return len(item1) == len(item2) and all((check_equality(a, b) for a, b in zip(item1, item2)))
    if isinstance(item1, dict):
        return item1.keys() == item2.keys() and all((check_equality(item1[k], item2[k]) for k in item1))
    if hasattr(item1, '__dict__'):
        return check_equality(item1.__dict__, item2.__dict__)
    return False
if __name__ == '__main__':
    print(check_equality(42, 42))
    print(check_equality('hello', 'world'))
    print(check_equality([1, 2, 3], [1, 2, 3]))
    print(check_equality({'a': 1}, {'a': 1}))
    print(check_equality({'a': 1}, {'b': 1}))