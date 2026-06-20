def are_values_equal(a, b):
    if a is None and b is None:
        return True
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a == b
    if isinstance(a, str) and isinstance(b, str):
        return a == b
    if isinstance(a, bool) and isinstance(b, bool):
        return a == b
    return False

if __name__ == '__main__':
    print(are_values_equal(10, 10))
    print(are_values_equal("hello", "hello"))
    print(are_values_equal(5.5, 5.5))
    print(are_values_equal(True, True))
    print(are_values_equal(1, 2))
    print(are_values_equal([1, 2], [1, 2]))
    print(are_values_equal(None, None))