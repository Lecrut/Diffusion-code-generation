def check_equality(value1, value2):
    try:
        return value1 == value2
    except Exception as e:
        print(f"Error during comparison: {e}")
        return False

if __name__ == '__main__':
    print(check_equality(10, 10))
    print(check_equality(5.5, 5.5))
    print(check_equality("hello", "hello"))
    print(check_equality(1, 2))
    print(check_equality(True, True))
    print(check_equality([1, 2], [1, 2]))