import sys
def are_chars_unique(s: str) -> bool:
    return len(set(s)) == len(s)
if __name__ == '__main__':
    test_cases = ["hello", "abcdefg", "", "a"]
    for case in test_cases:
        result = are_chars_unique(case)
        print(f"{case!r}: {result}")