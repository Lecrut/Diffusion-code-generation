def is_palindrome(text: str) -> bool:
    cleaned = text.lower()
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    print(is_palindrome("Racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("A man a plan a canal Panama"))