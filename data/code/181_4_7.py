class VowelWordFilter:
    def __init__(self, documents):
        self.documents = documents

    def is_vowel_char(self, char):
        return char.lower() in 'aeiou'

    def filter_vowel_words(self):
        vowels = "aeiouAEIOU"
        filtered_words = []
        for doc in self.documents:
            words = doc.split()
            vowel_words = [word for word in words if any(self.is_vowel_char(char) for char in word)]
            filtered_words.extend(vowel_words)
        return filtered_words

if __name__ == '__main__':
    documents = [
        "This is a test document.",
        "Another example with some vowels."
    ]
    filter_instance = VowelWordFilter(documents)
    print(filter_instance.filter_vowel_words())