import re

class DictionaryChecker:
    PUNCTUATION = r'[^\w\s]'

    @staticmethod
    def clean_text(text):
        return re.sub(DictionaryChecker.PUNCTUATION, '', text).lower()

    @classmethod
    def contains_word(cls, dictionary, word):
        cleaned_word = cls.clean_text(word)
        return any(cleaned_word == cls.clean_text(item) for item in dictionary)

if __name__ == '__main__':
    dictionary1 = ["apple", "banana", "cherry"]
    word1 = "Apple"
    result1 = DictionaryChecker.contains_word(dictionary1, word1)
    print(f"'{word1}' in {dictionary1}: {result1}")

    dictionary2 = ["hello", "world", "python"]
    word2 = "Python"
    result2 = DictionaryChecker.contains_word(dictionary2, word2)
    print(f"'{word2}' in {dictionary2}: {result2}")

    dictionary3 = ["programming", "is", "fun"]
    word3 = "Fun"
    result3 = DictionaryChecker.contains_word(dictionary3, word3)
    print(f"'{word3}' in {dictionary3}: {result3}")