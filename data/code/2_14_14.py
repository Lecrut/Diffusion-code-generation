def is_palindrome(s):
    s = s.lower().replace(" ", "")
    half_len = len(s) // 2
    for i in range(half_len):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("A man a plan a canal Panama"))
    print(is_palindrome("Python"))
    print(is_palindrome("Madam"))