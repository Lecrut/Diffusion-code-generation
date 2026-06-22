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
    sample_strings = ["radar", "hello", "madam", "python", "racecar", "a", ""]
    for s in sample_strings:
        print(is_palindrome(s))