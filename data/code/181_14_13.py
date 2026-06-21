class VowelFilter:
    def __init__(self):
        self.vowels = "aeiouAEIOU"

    def filter_words(self, words):
        return [word for word in words if any(char in self.vowels for char in word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    vowel_filter = VowelFilter()
    filtered_words = vowel_filter.filter_words(sample_words)
    print(filtered_words)