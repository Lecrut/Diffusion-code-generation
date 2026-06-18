def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    test_strings = ["racecar", "hello", "a", "abba"]
    for word in test_strings:
        print(f"{word}: {is_palindrome(word)}")