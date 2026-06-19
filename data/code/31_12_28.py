class StringChecker:

    def check(self, text):
        normalized_text = ''.join((c.lower() for c in text if c.isalnum()))
        return normalized_text == normalized_text[::-1]
if __name__ == '__main__':
    checker = StringChecker()
    sample_values = ['', 'A man, a plan, a canal: Panama', 'racecar', 'No lemon, no melon', 'Hello, World!']
    for value in sample_values:
        print(f"'{value}' is palindrome: {checker.check(value)}")