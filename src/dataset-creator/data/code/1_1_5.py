def has_uppercase(s: str) -> bool:
    return any(char.isupper() for char in s)
if __name__ == '__main__':
    test_strings = ["hello", "WORLD", "", "aBc"]
    for string in test_strings:
        print(f"{string!r}: {has_uppercase(string)}")