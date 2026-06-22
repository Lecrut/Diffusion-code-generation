def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = ["radar", "hello", "A man a plan a canal Panama".lower().replace(" ", ""), "noon", "python"]
    for case in test_cases:
        print(f"{case}: {is_palindrome(case)}")