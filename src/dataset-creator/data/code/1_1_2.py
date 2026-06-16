def has_uppercase(s: str) -> bool:
    return any(char.isupper() for char in s)
if __name__ == '__main__':
    test_cases = [
        ("Hello", True),
        ("hello", False),
        ("HELLO WORLD", True),
        ("123abc", False),
        ("", False),
        ("AaBbCc", True)
    ]
    for string, expected in test_cases:
        result = has_uppercase(string)
        print(f"Input: '{string}' -> Expected: {expected}, Got: {result}")