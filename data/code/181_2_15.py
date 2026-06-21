class VowelFilter:
    def __init__(self):
        self.vowels = set('aeiouAEIOU')

    def filter_words(self, words):
        return [word for word in words if any(char in self.vowels for char in word)]

if __name__ == '__main__':
    vowel_filter = VowelFilter()
    sample_words = ['hello', 'world', 'Python', 'programming', 'is', 'fun']
    filtered_words = vowel_filter.filter_words(sample_words)
    print(filtered_words)