class StringChecker:
    def contains_word(self, text, word):
        return word in text
if __name__ == '__main__':
    checker = StringChecker()
    text1 = "This is a sample text."
    word1 = "sample"
    result1 = checker.contains_word(text1, word1)
    print(f"Does '{text1}' contain '{word1}': {result1}")
    text2 = "Hello world"
    word2 = "python"
    result2 = checker.contains_word(text2, word2)
    print(f"Does '{text2}' contain '{word2}': {result2}")
    text3 = "programming is fun"
    word3 = "fun"
    result3 = checker.contains_word(text3, word3)
    print(f"Does '{text3}' contain '{word3}': {result3}")