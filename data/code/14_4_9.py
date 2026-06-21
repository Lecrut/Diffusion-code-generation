def has_duplicate_chars(s: str) -> bool:
    return len(s) != len(set(s))

if __name__ == '__main__':
    test_string = "programming"
    result = has_duplicate_chars(test_string)
    print(result)