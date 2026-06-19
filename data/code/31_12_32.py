class StringChecker:

    def check(self, text):
        normalized_text = text.lower()
        return normalized_text == normalized_text[::-1]
if __name__ == '__main__':
    checker = StringChecker()
    sample_values = ['', 'A man a plan a canal Panama', 'No lemon, no melon', 'Hello', 'Was it a car or a cat I saw?']
    results = [checker.check(value) for value in sample_values]
    print(results)