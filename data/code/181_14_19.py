class VowelFilter:
    def __init__(self):
        self.vowels = set("aeiouAEIOU")

    def filter_vowel_words(self, words):
        return [word for word in words if any(char in self.vowels for char in word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    vowel_filter = VowelFilter()
    print(vowel_filter.filter_vowel_words(sample_words))