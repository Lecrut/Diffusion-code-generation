def contains_repeated_chars(text):
    seen = set()
    for char in text:
        if char.lower() in seen:
            return True
        seen.add(char.lower())
    return False
if __name__ == '__main__':
    sample_strings = ["Hello", "PythonScript", "abcdefg"]
    test_cases = [
        ("Hello", True),
        ("PythonScript", True),
        ("abcdefg", False)
    ]
    for text, expected in test_cases:
        result = contains_repeated_chars(text)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: '{text}' -> {result} (expected {expected})")