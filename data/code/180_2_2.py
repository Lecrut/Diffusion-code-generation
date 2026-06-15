class StringChecker:
    def contains_word(self, text, word):
        return word in text
if __name__ == '__main__':
    checker = StringChecker()
    text1 = "The quick brown fox jumps over the lazy dog"
    word1 = "fox"
    result1 = checker.contains_word(text1, word1)
    print(f"'{word1}' in '{text1}': {result1}")
    text2 = "Programming is fun"
    word2 = "python"
    result2 = checker.contains_word(text2, word2)
    print(f"'{word2}' in '{text2}': {result2}")
    text3 = "hello world"
    word3 = "goodbye"
    result3 = checker.contains_word(text3, word3)
    print(f"'{word3}' in '{text3}': {result3}")