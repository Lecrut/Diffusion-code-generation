class StringChecker:
    def check(self, text):
        normalized_text = self._normalize(text)
        return self._is_palindrome(normalized_text)

    def _normalize(self, text):
        return ''.join(char.lower() for char in text if char.isalnum())

    def _is_palindrome(self, text):
        return text == text[::-1]

if __name__ == '__main__':
    checker = StringChecker()
    sample_values = ['', 'Able was I, I saw Elba', 'Madam In Eden, I’m Adam', 'Step on no pets', 'Was it a car or a cat I saw?']
    for value in sample_values:
        result = checker.check(value)
        print(f"'{value}' is a palindrome: {result}")