class StringProcessor:
    @staticmethod
    def extract_alphanumeric_words(phrase):
        import re
        words = re.findall(r'[a-zA-Z0-9]+', phrase)
        return words
if __name__ == '__main__':
    test_phrase = "Hello world, this is a test phrase 123 and more."
    result = StringProcessor.extract_alphanumeric_words(test_phrase)
    print(result)