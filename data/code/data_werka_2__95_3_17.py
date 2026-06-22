def validate_number(n):
    if n <= 0:
        return False
    if n >= 100:
        return False
    if n % 2 != 0:
        return False
    return True

if __name__ == '__main__':
    results = {
        "zero": validate_number(0),
        "two": validate_number(2),
        "fifty": validate_number(50),
        "ninety_nine": validate_number(99),
        "one_hundred": validate_number(100),
        "minus_five": validate_number(-5)
    }
    for key, val in results.items():
        print(f"{key}: {val}")