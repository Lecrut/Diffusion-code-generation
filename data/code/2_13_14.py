def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = ["racecar", "hello", "A man a plan a canal Panama", "Noon", "Python"]
    for text in test_cases:
        cleaned_text = text.replace(" ", "").lower()
        result = is_palindrome(cleaned_text)
        print(f"{text}: {result}")