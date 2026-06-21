class StringChecker:
    def check(self, text):
        normalized_text = ''.join(c.lower() for c in text if c.isalnum())
        return normalized_text == normalized_text[::-1]

if __name__ == '__main__':
    checker = StringChecker()
    sample_values = ['', 'A man a plan a canal Panama', 'No lemon, no melon', 'Hello', 'Was it a car or a cat I saw?']
    for value in sample_values:
        result = checker.check(value)
        print(f"'{value}' is a palindrome: {result}")