def is_valid_binary(s):
    if not isinstance(s, str):
        return False
    for char in s:
        if char != '0' and char != '1':
            return False
    return True
if __name__ == '__main__':
    test_cases = ["101", "000", "", "abc", 123, None]
    for case in test_cases:
        result = is_valid_binary(case)
        print(f"Input: {case!r} -> Valid Binary: {result}")