class StringChecker:
    ALPHABETIC_CHARS = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    @staticmethod
    def is_alphabetic(char):
        return char in StringChecker.ALPHABETIC_CHARS

    def check(self, text):
        filtered_chars = [char.lower() for char in text if self.is_alphabetic(char)]
        normalized_text = ''.join(filtered_chars)
        return normalized_text == normalized_text[::-1]

if __name__ == '__main__':
    checker = StringChecker()
    sample_values = ['', 'A man a plan a canal Panama', 'No lemon, no melon', 'Hello, World!', 'Was it a car or a cat I saw?']
    for value in sample_values:
        result = checker.check(value)
        print(f"'{value}' is a palindrome: {result}")