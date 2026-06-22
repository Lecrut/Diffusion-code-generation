def is_palindrome(s: str) -> bool:
    s = s.lower()
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("race a car"))
    print(is_palindrome(""))
    print(is_palindrome(" "))
    print(is_palindrome("a"))
    print(is_palindrome("Was it a car or a cat I saw?"))
    print(is_palindrome("No 'x' in Nixon"))
    print(is_palindrome("12321"))
    print(is_palindrome("12345"))
    print(is_palindrome("RaceCar"))