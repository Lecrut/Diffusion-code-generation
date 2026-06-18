def has_repeated_characters(s: str) -> bool:
    return len(set(s.lower())) < len(s)
if __name__ == '__main__':
    test_string = "Hello World"
    result = has_repeated_characters(test_string)
    print(f"'{test_string}' contains repeated characters: {result}")