def robust_strip(value):
    if value is None:
        return None
    if not isinstance(value, str):
        value = str(value)
    return value.strip()

if __name__ == '__main__':
    test_cases = [
        "  hello world  ",
        123,
        None,
        45.67,
        "   ",
        ["a", "b"]
    ]
    results = []
    for item in test_cases:
        results.append(robust_strip(item))
    print(results)