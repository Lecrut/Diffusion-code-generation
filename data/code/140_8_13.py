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
    sample_values = ["radar", "hello", "level", "world"]
    for value in sample_values:
        print(f"'{value}' is a palindrome: {is_palindrome(value)}")