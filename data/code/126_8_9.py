def are_values_equal(a, b):
    if not isinstance(a, (int, str)) or not isinstance(b, (int, str)):
        raise ValueError("Both inputs must be either int or str")
    return a == b

if __name__ == '__main__':
    print(are_values_equal(5, 5))
    print(are_values_equal(3, 7))
    print(are_values_equal("hello", "hello"))
    try:
        print(are_values_equal([1, 2], [1, 2]))
    except ValueError as e:
        print(e)