def is_palindrome(s: str) -> bool:
    s = s.lower()
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    sample_strings = ["Racecar", "hello", "A man a plan a canal Panama"]
    for text in sample_strings:
        result = is_palindrome(text)
        print(f"is_palindrome('{text}') = {result}")