class VowelWordFilter:
    def __init__(self, documents):
        self.documents = documents

    @staticmethod
    def _is_vowel(char):
        return char.lower() in 'aeiou'

    def filter_vowel_words(self):
        filtered_words = []
        for doc in self.documents:
            words = doc.split()
            vowel_words = [word for word in words if any(self._is_vowel(char) for char in word)]
            filtered_words.extend(vowel_words)
        return filtered_words

if __name__ == '__main__':
    sample_documents = [
        "Hello world, this is a test.",
        "Python programming is fun!",
        "Vowels are important in language."
    ]
    filter_instance = VowelWordFilter(sample_documents)
    print(filter_instance.filter_vowel_words())