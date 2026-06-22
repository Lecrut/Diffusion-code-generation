def is_palindrome(text: str) -> bool:
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    sample1 = "racecar"
    sample2 = "hello"
    print(is_palindrome(sample1))
    print(is_palindrome(sample2))