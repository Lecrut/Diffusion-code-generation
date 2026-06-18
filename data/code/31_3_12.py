def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    assert is_palindrome("racecar") == True and is_palindrome("hello") == False, "Test failed"