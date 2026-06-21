def has_unique_characters(s: str) -> bool:
    return len(set(s)) == len(s)

if __name__ == '__main__':
    test_string = "abcdefg"
    print(has_unique_characters(test_string))
    test_string_with_duplicates = "hello"
    print(has_unique_characters(test_string_with_duplicates))