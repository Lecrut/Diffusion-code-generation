class StringProcessor:
    @staticmethod
    def extract_alphanumeric_words(phrase):
        import re
        words = re.findall(r'[a-zA-Z0-9]+', phrase)
        return words
if __name__ == '__main__':
    test_phrase1 = "Hello world, this is a test sentence 123."
    result1 = StringProcessor.extract_alphanumeric_words(test_phrase1)
    print(f"Phrase: '{test_phrase1}'")
    print(f"Extracted words: {result1}")
    test_phrase2 = "AlphaBetaGamma 456XYZ and some punctuation!"
    result2 = StringProcessor.extract_alphanumeric_words(test_phrase2)
    print(f"Phrase: '{test_phrase2}'")
    print(f"Extracted words: {result2}")
    test_phrase3 = "NoWordsHere."
    result3 = StringProcessor.extract_alphanumeric_words(test_phrase3)
    print(f"Phrase: '{test_phrase3}'")
    print(f"Extracted words: {result3}")