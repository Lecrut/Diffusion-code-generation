def are_values_equal(value1, value2):
    if not isinstance(value1, (int, float, str)):
        raise ValueError("Unsupported type for comparison")
    if not isinstance(value2, (int, float, str)):
        raise ValueError("Unsupported type for comparison")
    return value1 == value2

if __name__ == '__main__':
    print(are_values_equal(5, 5))
    print(are_values_equal(3.0, 3.0))
    print(are_values_equal("hello", "hello"))
    print(are_values_equal("hello", "world"))
    try:
        print(are_values_equal([1, 2], [1, 2]))
    except ValueError as e:
        print(e)