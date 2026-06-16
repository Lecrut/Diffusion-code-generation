def has_uppercase(s: str) -> bool:
    return any(char.isupper() for char in s)
if __name__ == '__main__':
    test_cases = ["Hello", "hello", "", "HELLO WORLD"]
    for case in test_cases:
        print(f"'{case}': {has_uppercase(case)}")