class VowelFilter:
    VOWELS = set('aeiouAEIOU')

    @staticmethod
    def contains_vowel(word):
        return any(char in VowelFilter.VOWELS for char in word)

    @classmethod
    def filter_vowel_words(cls, words):
        return [word for word in words if cls.contains_vowel(word)]

if __name__ == '__main__':
    test_words = ['hello', 'world', 'Python', 'programming', 'is', 'fun']
    filtered_words = VowelFilter.filter_vowel_words(test_words)
    print(filtered_words)