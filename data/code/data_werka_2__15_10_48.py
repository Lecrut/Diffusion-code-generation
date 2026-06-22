def validate_and_check_equality(a, b):
    if not isinstance(a, (int, float, str, list, dict, tuple)):
        raise ValueError("Unsupported type for comparison")
    return a == b

if __name__ == '__main__':
    print(validate_and_check_equality(10, 10))          # True
    print(validate_and_check_equality("hello", "world"))  # False
    print(validate_and_check_equality([1, 2], [1, 2]))    # True
    print(validate_and_check_equality({"a": 1}, {"b": 1}))# False