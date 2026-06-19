def check_equality(item1, item2):
    if item1 is item2:
        return True
    elif isinstance(item1, type(item2)) and isinstance(item2, type(item1)):
        if isinstance(item1, dict):
            return item1 == item2 and all((check_equality(v1, v2) for v1, v2 in zip(item1.values(), item2.values())))
        elif isinstance(item1, (list, set, tuple)):
            return len(item1) == len(item2) and all((check_equality(i1, i2) for i1, i2 in zip(sorted(item1), sorted(item2))))
        else:
            return item1 == item2
    return False
if __name__ == '__main__':
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = (1, 2, 3)
    d = {1, 2, 3}
    e = {'a': 1, 'b': 2}
    f = {'b': 2, 'a': 1}
    print(check_equality(a, b))
    print(check_equality(b, c))
    print(check_equality(c, d))
    print(check_equality(d, a))
    print(check_equality(e, f))