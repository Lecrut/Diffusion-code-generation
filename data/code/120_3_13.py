def are_values_equal(val1, val2):
    if not isinstance(val1, (int, float, str)) or not isinstance(val2, (int, float, str)):
        raise ValueError("Both values must be int, float, or str")
    return val1 == val2

if __name__ == '__main__':
    print(are_values_equal(5, 5))
    print(are_values_equal(10, 5))
    print(are_values_equal("hello", "hello"))
    print(are_values_equal(3.14, 3.1400000000000004))