def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    result = is_palindrome("racecar")
    print(result)