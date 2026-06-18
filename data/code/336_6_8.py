from collections import Counter
def is_unique(s: str) -> bool:
    return len(set(s)) == len(s)
if __name__ == '__main__':
    test_cases = ["abcdef", "hello"]
    for case in test_cases:
        result = is_unique(case)
        print(f"{case}: {result}")