def are_equal(var1, var2):
    if type(var1) != type(var2):
        return False
    if isinstance(var1, (int, float, str)):
        return var1 == var2
    if isinstance(var1, list):
        if len(var1) != len(var2):
            return False
        for v1, v2 in zip(var1, var2):
            if not are_equal(v1, v2):
                return False
        return True
    if isinstance(var1, dict):
        if len(var1) != len(var2):
            return False
        for key in var1:
            if key not in var2 or not are_equal(var1[key], var2[key]):
                return False
        return True
    return var1 is var2

if __name__ == '__main__':
    print(are_equal(5, 5))
    print(are_equal(5, 6))
    print(are_equal('hello', 'hello'))
    print(are_equal('hello', 'world'))
    print(are_equal([1, 2], [1, 2]))
    print(are_equal([1, 2], [1, 3]))
    print(are_equal({'a': 1}, {'a': 1}))
    print(are_equal({'a': 1}, {'b': 1}))