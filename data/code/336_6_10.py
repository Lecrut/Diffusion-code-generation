def is_unique(s):
    return len(set(s)) == len(s)
if __name__ == '__main__':
    test_cases = ["abcdef", "hello", "12345"]
    for case in test_cases:
        result = is_unique(case)
        print(f"{case}: {result}")