def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    sample1 = "racecar"
    sample2 = "hello"
    sample3 = "A"
    result1 = is_palindrome(sample1)
    result2 = is_palindrome(sample2)
    result3 = is_palindrome(sample3)
    print(result1)
    print(result2)
    print(result3)