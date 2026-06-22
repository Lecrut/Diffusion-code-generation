def check_equality(a, b):
    if a is None and b is None:
        return True
    elif a is None or b is None:
        return False
    else:
        return a == b

if __name__ == '__main__':
    value1 = 42
    value2 = 42
    result = check_equality(value1, value2)
    print(result)

    value3 = None
    value4 = None
    result = check_equality(value3, value4)
    print(result)

    value5 = "hello"
    value6 = "world"
    result = check_equality(value5, value6)
    print(result)

    value7 = [1, 2, 3]
    value8 = [1, 2, 3]
    result = check_equality(value7, value8)
    print(result)