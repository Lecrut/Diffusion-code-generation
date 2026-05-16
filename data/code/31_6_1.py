def is_palindrome(s):
    if not s:
        return True
    processed_s = "".join(filter(str.isalnum, s)).lower()
    return processed_s == processed_s[::-1]
if __name__ == '__main__':
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("", True),
        ("a", True),
        ("aba", True),
        ("Madam", True),
        ("A man, a plan, a canal: Panama", True),
        ("121", True),
        ("12321", True),
        (" ", True),
        ("!@#$%^&*", True),
        ("abcde", False),
        ("1a2b1", False)
    ]
    for input_str, expected in test_cases:
        result = is_palindrome(input_str)
        assert result == expected, f"Input: '{input_str}', Expected: {expected}, Got: {result}"
        print(f"Input: '{input_str}', Result: {result}, Expected: {expected} - PASS")