import sys
def is_unique(s: str) -> bool:
    return len(set(s)) == len(s)
if __name__ == '__main__':
    test_cases = ["hello", "abcdefg", "", "a"]
    for case in test_cases:
        result = is_unique(case)
        print(f"'{case}': {result}")