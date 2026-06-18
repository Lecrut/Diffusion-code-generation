def is_palindrome(s: str) -> bool:
    return s == ''.join(c.lower() if c.isalnum() else '' for c in reversed(s))

if __name__ == '__main__':
    test_cases = ["A man, a plan, a canal: Panama", "race car", "hello world"]
    for case in test_cases:
        print(f"{case!r} -> {is_palindrome(case)}")