def check_equality(val1, val2):
    return val1 == val2

if __name__ == '__main__':
    value_pairs = {
        (10, 10): True,
        (5, 8): False,
        ("hello", "hello"): True,
        (3.14, 3.140000000000001): False
    }

    for (val1, val2), expected in value_pairs.items():
        result = check_equality(val1, val2)
        print(f"Checking {val1} and {val2}: {result == expected}")