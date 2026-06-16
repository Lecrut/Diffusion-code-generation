def has_uppercase(s: str) -> bool:
    return any(c.isupper() for c in s)
if __name__ == '__main__':
    test_cases = ["Hello", "hello", "", "HELLO WORLD"]
    for case in test_cases:
        print(f"'{case}': {has_uppercase(case)}")