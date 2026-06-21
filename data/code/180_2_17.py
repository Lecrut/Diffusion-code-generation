import re
PUNCTUATION = '[^\\w\\s]'

class WordChecker:

    def contains_word(self, text, word):
        cleaned_text = re.sub(PUNCTUATION, '', text).lower()
        cleaned_word = word.lower()
        return cleaned_word in cleaned_text
if __name__ == '__main__':
    checker = WordChecker()
    text1 = 'This is a sample text.'
    word1 = 'sample'
    result1 = checker.contains_word(text1, word1)
    print(f"'{word1}' in '{text1}': {result1}")
    text2 = 'Hello world!'
    word2 = 'python'
    result2 = checker.contains_word(text2, word2)
    print(f"'{word2}' in '{text2}': {result2}")
    text3 = 'programming is fun.'
    word3 = 'fun'
    result3 = checker.contains_word(text3, word3)
    print(f"'{word3}' in '{text3}': {result3}")