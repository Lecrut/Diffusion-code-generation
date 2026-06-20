def is_equal(a, b):
    if not isinstance(a, (int, float, str)) or not isinstance(b, (int, float, str)):
        raise ValueError("Both arguments must be int, float, or str")
    return a == b

if __name__ == '__main__':
    print(is_equal(5, 5))
    print(is_equal(10, 5))
    print(is_equal("hello", "hello"))
    try:
        print(is_equal([1, 2], [1, 2]))
    except ValueError as e:
        print(e)