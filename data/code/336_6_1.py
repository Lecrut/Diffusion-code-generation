import sys
def is_unique(s: str) -> bool:
    return len(set(s)) == len(s)
if __name__ == '__main__':
    test_strings = ["hello", "abcdefg", "12345"]
    for s in test_strings:
        result = is_unique(s)
        print(f"{s}: {result}")