class VowelFilter:
    def __init__(self, documents):
        self.documents = documents

    def filter_vowel_words(self):
        vowels = "aeiouAEIOU"
        filtered_words = []
        for doc in self.documents:
            words = doc.split()
            vowel_words = [word for word in words if any(char in vowels for char in word)]
            filtered_words.extend(vowel_words)
        return filtered_words

if __name__ == '__main__':
    documents = [
        "This is a test document.",
        "Another example with some vowels."
    ]
    vowel_filter = VowelFilter(documents)
    print(vowel_filter.filter_vowel_words())