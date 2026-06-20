def are_values_equivalent(value1, value2):
    return value1 == value2

if __name__ == '__main__':
    print(are_values_equivalent(42, 42))
    print(are_values_equivalent("hello", "hello"))
    print(are_values_equivalent([1, 2, 3], [1, 2, 3]))
    print(are_values_equivalent({"a": 1}, {"a": 1}))
    print(are_values_equivalent(None, None))
    print(are_values_equivalent(True, True))
    print(are_values_equivalent(False, False))