class WordFilter:
    VOWELS = "aeiouAEIOU"

    @staticmethod
    def has_vowels(word):
        return any(char in WordFilter.VOWELS for char in word)

    @staticmethod
    def filter_vowel_words(words):
        return [word for word in words if WordFilter.has_vowels(word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    result = WordFilter.filter_vowel_words(sample_words)
    print(result)