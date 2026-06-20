def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    test_strings = ["radar", "hello", "A man a plan a canal Panama", "racecar", "world"]
    for text in test_strings:
        clean_text = ''.join(c.lower() for c in text if c.isalnum())
        result = is_palindrome(clean_text)
        print(f"{text}: {result}")