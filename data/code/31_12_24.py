class StringChecker:

    def check(self, text):
        normalized_text = text.lower()
        return normalized_text == normalized_text[::-1]
if __name__ == '__main__':
    checker = StringChecker()
    sample_texts = ['', 'A man a plan a canal Panama', 'No lemon no melon', 'Hello World']
    for text in sample_texts:
        print(f"'{text}' is palindrome: {checker.check(text)}")