def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = [
        "racecar",
        "hello",
        "A man a plan a canal Panama".lower().replace(" ", "").replace("-", ""),  # Note: task says only alphanumeric, but this is for testing logic if spaces were present; strictly per task s has no non-alnum. Let's use pure alnum examples.
    ]
    # Corrected test cases adhering to "only contains alphanumeric" and already lowercase assumption
    valid_test_cases = [
        "racecar",
        "madam",
        "abcdefg",
        "noon",
    ]

    for s in valid_test_cases:
        print(f"{s!r} is {'a' if is_palindrome(s) else 'not'} a palindrome")