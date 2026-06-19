class PalindromeChecker:
    def is_palindrome(self, text):
        if not text:
            return True
        cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
        return cleaned_text == cleaned_text[::-1]

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