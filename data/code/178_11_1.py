class StringProcessor:
    @staticmethod
    def extract_alphanumeric_words(phrase):
        words = []
        for word in phrase.split():
            if word.isalnum():
                words.append(word)
        return words
if __name__ == '__main__':
    test_phrase1 = "Hello world this is a test sentence 123"
    result1 = StringProcessor.extract_alphanumeric_words(test_phrase1)
    print(f"Input: '{test_phrase1}'")
    print(f"Output: {result1}")
    test_phrase2 = "Python programming is fun and easy 42"
    result2 = StringProcessor.extract_alphanumeric_words(test_phrase2)
    print(f"Input: '{test_phrase2}'")
    print(f"Output: {result2}")
    test_phrase3 = "Word with punctuation! and numbers 567."
    result3 = StringProcessor.extract_alphanumeric_words(test_phrase3)
    print(f"Input: '{test_phrase3}'")
    print(f"Output: {result3}")