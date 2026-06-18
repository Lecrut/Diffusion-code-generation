def get_string_length(s: str) -> int:
    return len(s)

if __name__ == '__main__':
    test_strings = ["", "hello", "!@#"]
    print([get_string_length(s) for s in test_strings])