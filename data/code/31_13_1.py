class StringChecker:
    def check(self, text):
        if not text:
            return True
        processed_text = "".join(filter(str.isalnum, text)).lower()
        return processed_text == processed_text[::-1]
if __name__ == '__main__':
    checker = StringChecker()
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("", True),
        ("Madam", True),
        ("A man, a plan, a canal: Panama", True),
        ("No lemon, no melon", True),
        ("121", True),
        ("abcde", False),
        ("aba", True),
        ("Was it a car or a cat I saw", True),
        ("1a2", False)
    ]
    for text, expected in test_cases:
        result = checker.check(text)
        print(f"Input: '{text}', Expected: {expected}, Got: {result}, Match: {result == expected}")