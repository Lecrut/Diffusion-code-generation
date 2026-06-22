def has_unique_characters(s: str) -> bool:
    return len(s) == len(set(s))

if __name__ == '__main__':
    test_string_1 = "abcdef"
    test_string_2 = "hello"
    print(has_unique_characters(test_string_1))
    print(has_unique_characters(test_string_2))