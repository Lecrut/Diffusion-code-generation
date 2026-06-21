class VowelFilter:
    def __init__(self, documents):
        self.documents = documents

    def filter_vowel_words(self):
        vowels = "aeiouAEIOU"
        return [word for doc in self.documents for word in doc.split() if any(char in vowels for char in word)]

if __name__ == '__main__':
    sample_documents = [
        "Hello world, this is a test.",
        "Python programming is fun!",
        "Vowels are important in language."
    ]
    vowel_filter = VowelFilter(sample_documents)
    print(vowel_filter.filter_vowel_words())