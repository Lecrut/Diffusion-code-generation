class VowelWordFilter:
    def __init__(self, documents):
        self.documents = documents
    
    @staticmethod
    def _is_vowel(word):
        vowels = 'aeiouAEIOU'
        return any(char in vowels for char in word)
    
    def filter_vowel_words(self):
        filtered_words = []
        for doc in self.documents:
            words = doc.split()
            vowel_words = [word for word in words if self._is_vowel(word)]
            filtered_words.extend(vowel_words)
        return filtered_words

if __name__ == '__main__':
    documents = [
        "This is a test document.",
        "Another example with some vowels."
    ]
    filter_instance = VowelWordFilter(documents)
    print(filter_instance.filter_vowel_words())