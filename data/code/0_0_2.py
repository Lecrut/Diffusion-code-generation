def extract_digits_to_int(s):
    digits = [char for char in s if char.isdigit()]
    if not digits:
        return 0
    return int("".join(digits))

if __name__ == "__main__":
    test_cases = [
        "abc123def",
        "no_digits_here",
        "9876543210",
        "mixed99and77",
        "",
        "a1b2c3"
    ]
    for case in test_cases:
        result = extract_digits_to_int(case)
        print(result)