class StringChecker:

    def check(self, text):
        normalized_text = ''.join((char.lower() for char in text if char.isalnum()))
        return normalized_text == normalized_text[::-1]
if __name__ == '__main__':
    checker = StringChecker()
    sample_values = ['', 'A man, a plan, a canal: Panama', 'racecar', 'hello', 'No lemon, no melon']
    for value in sample_values:
        result = checker.check(value)
        print(f"'{value}' is a palindrome: {result}")