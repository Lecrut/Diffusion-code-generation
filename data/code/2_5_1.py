def is_palindrome(s: str) -> bool:
    cleaned = s.lower()
    left = 0
    right = len(cleaned) - 1
    while left < right:
        while left < right and not cleaned[left].isalnum():
            left += 1
        while left < right and not cleaned[right].isalnum():
            right -= 1
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    print(is_palindrome("Racecar"))
    print(is_palindrome("Hello"))
    print(is_palindrome("A man, a plan, a canal: Panama"))