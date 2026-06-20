def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    test_cases = ["racecar", "hello", "A man a plan a canal Panama", "madam"]
    for text in test_cases:
        cleaned = text.replace(" ", "").lower()
        print(cleaned, is_palindrome(cleaned))