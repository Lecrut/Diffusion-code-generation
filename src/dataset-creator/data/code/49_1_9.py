def get_sign(value):
    if value is None:
        return 0
    try:
        num = float(value)
    except (ValueError, TypeError):
        return 0
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0
if __name__ == '__main__':
    test_values = [5, -3.5, "hello", None, True]
    for val in test_values:
        print(f"{val}: {get_sign(val)}")