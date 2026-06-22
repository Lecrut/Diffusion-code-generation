class StringChecker:
    def check(self, text):
        normalized_text = self._normalize(text)
        return normalized_text == normalized_text[::-1]

    def _normalize(self, text):
        return ''.join(char.lower() for char in text if char.isalnum())

if __name__ == '__main__':
    checker = StringChecker()
    sample_values = ['', 'A man a plan a canal Panama', 'No lemon, no melon', 'Hello', 'Was it a car or a cat I saw?']
    for value in sample_values:
        result = checker.check(value)
        print(f"'{value}' is a palindrome: {result}")