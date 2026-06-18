def is_palindrome(s: str) -> bool:
    return s == "".join(reversed(list(filter(str.isalnum, s)))) if isinstance(s, str) else False

if __name__ == '__main__':
    test_cases = ["A man a plan a canal Panama", "race car", "hello world"]
    for case in test_cases:
        # Pre-process as per assumption (alphanumeric only + lowercase), though task says input is already done.
        processed = "".join(c.lower() if c.isalnum() else '' for c in case)
        print(f"{case!r} -> {is_palindrome(processed)}")