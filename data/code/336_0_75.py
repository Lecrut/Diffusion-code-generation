import sys
def has_repeated_chars(text: str) -> bool:
    seen = set()
    for char in text.lower():
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    sample_strings = ["hello", "abcdefg", "AaBbCc"]
    test_cases = [
        ("hello", True),
        ("abcdefg", False),
        ("AaBbCc", True),
        ("Python3.12", False)
    ]
    for input_str, expected in test_cases:
        result = has_repeated_chars(input_str)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: '{input_str}' -> {result}")