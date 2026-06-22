def is_alphanumeric_only(s: str) -> bool:
    if not s:
        return True
    for char in s:
        if not char.isalnum():
            return False
    return True

if __name__ == '__main__':
    test_strings = ["Hello123", "Hello World!", "abcXYZ", "12345", "Test-String"]
    for s in test_strings:
        result = is_alphanumeric_only(s)
        print(result)