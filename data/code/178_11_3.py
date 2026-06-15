class StringProcessor:
    @staticmethod
    def extract_alphanumeric_words(phrase):
        import re
        words = re.findall(r'[a-zA-Z0-9]+', phrase)
        return words
if __name__ == '__main__':
    test_phrase1 = "Hello World 123 Python programming"
    result1 = StringProcessor.extract_alphanumeric_words(test_phrase1)
    print(f"Input: '{test_phrase1}'")
    print(f"Output: {result1}")
    test_phrase2 = "This is a test sentence with numbers like 456 and words."
    result2 = StringProcessor.extract_alphanumeric_words(test_phrase2)
    print(f"Input: '{test_phrase2}'")
    print(f"Output: {result2}")
    test_phrase3 = "NoWordsHere!"
    result3 = StringProcessor.extract_alphanumeric_words(test_phrase3)
    print(f"Input: '{test_phrase3}'")
    print(f"Output: {result3}")