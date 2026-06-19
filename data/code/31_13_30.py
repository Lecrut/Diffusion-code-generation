class PalindromeChecker:
    def is_palindrome(self, text):
        processed_text = ''.join(filter(str.isalnum, text)).lower()
        return processed_text == processed_text[::-1]

if __name__ == '__main__':
    checker = PalindromeChecker()
    sample_values = [
        ("A Santa at NASA", True),
        ("Was it a car or a cat I saw?", False),
        ("No lemon, no melon", True),
        ("", True),
        ("Madam", True),
        ("12321", True),
        ("racecar", True),
        ("hello", False)
    ]

    for text, expected in sample_values:
        result = checker.is_palindrome(text)
        print(f"'{text}' -> {result} (Expected: {expected})")