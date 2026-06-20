def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    test_strings = ["racecar", "hello", "madam", "python"]
    results = [(s, is_palindrome(s)) for s in test_strings]
    for s, result in results:
        print(result)