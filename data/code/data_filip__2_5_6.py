def is_palindrome(s: str) -> bool:
    cleaned = s.lower()
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    print(is_palindrome("Racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("A man a plan a canal Panama"))
    print(is_palindrome("No lemon, no melon"))
    print(is_palindrome(""))
    print(is_palindrome("a"))
    print(is_palindrome("AbBa"))
    print(is_palindrome("Python"))