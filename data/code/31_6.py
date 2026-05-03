def is_palindrome(s):
    if not s:
        return True
    processed_s = ""
    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            processed_s += char.lower()
    if not processed_s:
        return True
    return processed_s == processed_s[::-1]
if __name__ == '__main__':
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("", True),
        ("a", True),
        ("ab", False),
        ("Madam", True),
        ("A man, a plan, a canal: Panama", True),
        ("121", True),
        ("!@#$%^&*", True),
        ("level", True),
        ("No lemon, no melon", True),
        ("abcde", False)
    ]
    for input_str, expected in test_cases:
        result = is_palindrome(input_str)
        assert result == expected, f"Input: '{input_str}', Expected: {expected}, Got: {result}"
        print(f"Input: '{input_str}', Result: {result}, Expected: {expected} - PASS")