def check_equality(value1, value2):
    try:
        return value1 == value2
    except TypeError as e:
        print(f"Error comparing values: {e}")
        return False

if __name__ == '__main__':
    print(check_equality(10, 10))
    print(check_equality(5.5, 5.5))
    print(check_equality("hello", "hello"))
    print(check_equality(1, 2))
    print(check_equality(True, True))
    print(check_equality(10, 10.0))
    print(check_equality(None, None))
    print(check_equality([1, 2], [1, 3]))