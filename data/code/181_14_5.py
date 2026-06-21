class WordFilter:
    VOWELS = "aeiouAEIOU"

    @staticmethod
    def contains_vowel(word):
        return any(char in WordFilter.VOWELS for char in word)

    @classmethod
    def filter_vowels(cls, words):
        return [word for word in words if cls.contains_vowel(word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    print(WordFilter.filter_vowels(sample_words))