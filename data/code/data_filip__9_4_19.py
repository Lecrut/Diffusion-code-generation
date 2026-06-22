def safe_strip(input_value):
    if input_value is None:
        return ""
    if not isinstance(input_value, str):
        input_value = str(input_value)
    return input_value.strip()

if __name__ == '__main__':
    test_cases = ["  hello  ", 123, None, "   ", 45.67, ["list"]]
    for case in test_cases:
        print(safe_strip(case))