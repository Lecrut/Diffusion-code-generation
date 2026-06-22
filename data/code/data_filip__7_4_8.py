import string

def find_first_special_char(s: str) -> str | None:
    special_chars = set(string.punctuation)
    for char in s:
        if char in special_chars:
            return char
    return None

if __name__ == '__main__':
    test_strings = ["hello world", "hello! world", "no_special_here", "@test"]
    for test in test_strings:
        result = find_first_special_char(test)
        print(result)