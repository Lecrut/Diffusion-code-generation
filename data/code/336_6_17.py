import sys
def has_unique_chars(s: str) -> bool:
    return len(set(s)) == len(s)
if __name__ == '__main__':
    test_strings = ["hello", "abcdefg", "", "12345"]
    for s in test_strings:
        result = has_unique_chars(s)
        print(f"'{s}': {result}")