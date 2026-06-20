def are_values_equal(a, b):
    try:
        return a == b
    except TypeError as e:
        print(f"Error: {e}")
        return False

if __name__ == '__main__':
    print(are_values_equal(10, 10))
    print(are_values_equal("hello", "hello"))
    print(are_values_equal(5.5, 5.5))
    print(are_values_equal(True, True))
    print(are_values_equal(1, 2))
    print(are_values_equal([1, 2], [1, 2]))
    print(are_values_equal(None, None))