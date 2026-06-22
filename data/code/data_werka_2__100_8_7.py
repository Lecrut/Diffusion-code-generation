def validate_and_compare(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numeric")
    if isinstance(a, bool) or isinstance(b, bool):
        raise ValueError("Inputs must be numeric")
    s = a + b
    d = a - b
    return s > d

if __name__ == '__main__':
    val_a = 5
    val_b = 3
    outcome = validate_and_compare(val_a, val_b)
    print(outcome)