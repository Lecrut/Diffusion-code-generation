def has_uppercase(s):
    return any(c.isupper() for c in s)
if __name__ == '__main__':
    test_cases = ["hello", "Hello", "HELLO", "", "123"]
    results = [has_uppercase(tc) for tc in test_cases]
    print(results)