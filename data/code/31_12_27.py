class StringChecker:

    def check(self, text):
        normalized_text = text.lower()
        return normalized_text == normalized_text[::-1]
if __name__ == '__main__':
    checker = StringChecker()
    sample_values = ['', 'A', 'Madam', 'racecar', 'hello', 'Was it a car or a cat I saw']
    results = {value: checker.check(value) for value in sample_values}
    print(results)