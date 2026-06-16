def has_uppercase(s: str) -> bool:
    return any(char.isupper() for char in s)
if __name__ == '__main__':
    test_cases = ["Hello", "world", "", "!@#", "Python3.9"]
    for case in test_cases:
        result = has_uppercase(case)
        print(f"String '{case}': {result}")