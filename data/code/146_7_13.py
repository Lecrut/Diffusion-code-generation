def is_palindrome(s):
    s = s.lower()
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    test_strings = ["radar", "hello", "A man a plan a canal Panama", "Was it a car or a cat I saw"]
    for string in test_strings:
        print(f"'{string}' is palindrome: {is_palindrome(string)}")