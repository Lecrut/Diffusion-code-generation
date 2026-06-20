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
    sample_values = ["racecar", "hello", "a", "abba", "abcba", "abccba", "python", "madam", "12321", ""]
    for value in sample_values:
        result = is_palindrome(value)
        print(f"is_palindrome({repr(value)}) = {result}")