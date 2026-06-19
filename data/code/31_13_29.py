class PalindromeChecker:
    def __init__(self):
        self.ALPHA_NUM = str.isalnum

    def is_palindrome(self, text):
        if not text:
            return True
        processed_text = ''.join(filter(self.ALPHA_NUM, text)).lower()
        return processed_text == processed_text[::-1]

if __name__ == '__main__':
    checker = PalindromeChecker()
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("", True),
        ("Madam", True),
        ("A man, a plan, a canal: Panama", True),
        ("No lemon, no melon", True),
        ("12321", True),
        ("abcde", False),
        ("level", True)
    ]
    for text, expected in test_cases:
        result = checker.is_palindrome(text)
        print(f"'{text}' is a palindrome: {result} (Expected: {expected})")