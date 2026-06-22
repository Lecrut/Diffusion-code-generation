class PalindromeChecker:
    def __init__(self):
        self.processed_text = ""

    def _is_alphanumeric(self, char):
        return char.isalnum()

    def _process_text(self, text):
        filtered_chars = filter(self._is_alphanumeric, text)
        self.processed_text = ''.join(filtered_chars).lower()
        return self.processed_text

    def check_palindrome(self, text):
        if not text:
            return True
        self._process_text(text)
        return self.processed_text == self.processed_text[::-1]

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
        result = checker.check_palindrome(text)
        print(f"'{text}' is a palindrome: {result} (Expected: {expected})")