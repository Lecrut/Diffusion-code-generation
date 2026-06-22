def validate_or_condition(left, right):
    if not isinstance(left, (int, float, str, bool, type(None), list, dict, tuple)):
        raise ValueError("Left operand must be a valid Python object")
    if not isinstance(right, (int, float, str, bool, type(None), list, dict, tuple)):
        raise ValueError("Right operand must be a valid Python object")
    return left or right

if __name__ == '__main__':
    samples = [
        (0, 1),
        (None, "hello"),
        (False, True),
        ([], [1, 2]),
        ("", "world"),
        (0, 0),
        (None, None),
        (False, False)
    ]
    for left, right in samples:
        result = validate_or_condition(left, right)
        print(result)