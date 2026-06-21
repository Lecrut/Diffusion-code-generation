class VowelFilter:
    def __init__(self):
        self.vowels = set('aeiouAEIOU')

    def filter_vowel_words(self, words):
        return [word for word in words if any(char in self.vowels for char in word)]

if __name__ == '__main__':
    filter_instance = VowelFilter()
    test_words = ['hello', 'world', 'Python', 'programming', 'is', 'fun']
    filtered_words = filter_instance.filter_vowel_words(test_words)
    print(filtered_words)