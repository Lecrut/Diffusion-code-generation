def is_palindrome(text):
    if text is None:
        return False
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    sample1 = "radar"
    sample2 = "hello"
    sample3 = "A man a plan a canal Panama"
    print(is_palindrome(sample1))
    print(is_palindrome(sample2))
    print(is_palindrome(sample3))