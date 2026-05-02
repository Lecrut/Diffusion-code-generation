def is_palindrome_optimized(s: str) -> bool:
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True
if __name__ == '__main__':
    test_strings = [
        "racecar",
        "hello",
        "madam",
        "a",
        "",
        "level",
        "abcde"
    ]
    for s in test_strings:
        result = is_palindrome_optimized(s)
        print(f"'{s}': {result}")