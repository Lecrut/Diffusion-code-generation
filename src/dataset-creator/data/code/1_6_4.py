def is_binary_string(s):
    if not isinstance(s, str):
        return False
    for char in s:
        if char != '0' and char != '1':
            return False
    return True
if __name__ == '__main__':
    test_cases = [
        "0",
        "1",
        "0101",
        "",
        123,
        None,
        ["0"],
        "abc"
    ]
    for case in test_cases:
        result = is_binary_string(case)
        print(f"{case!r}: {result}")