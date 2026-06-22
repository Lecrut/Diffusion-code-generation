def sanitize_to_float(mixed_string):
    digits_only = ""
    for char in mixed_string:
        if char.isdigit():
            digits_only += char
    if not digits_only:
        digits_only = "0"
    return float(digits_only)

if __name__ == '__main__':
    test_cases = ["abc123xyz", "$45.67", "9a8b7c", "no_digits_here", "007"]
    for case in test_cases:
        result = sanitize_to_float(case)
        print(f"Input: {case}, Output: {result}")