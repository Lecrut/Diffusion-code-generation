def is_palindrome(s):
    cleaned = s.lower()
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    print(is_palindrome("Racecar"))
    print(is_palindrome("Hello"))
    print(is_palindrome("A man a plan a canal Panama"))