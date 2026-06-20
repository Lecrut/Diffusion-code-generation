def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    print(is_palindrome("radar"))
    print(is_palindrome("hello"))
    print(is_palindrome("A man a plan a canal Panama"))