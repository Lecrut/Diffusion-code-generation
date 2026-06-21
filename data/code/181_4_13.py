class VowelWordSelector:
    def __init__(self, documents):
        self.documents = documents

    def filter_vowel_words(self):
        vowels = "aeiouAEIOU"
        filtered_words = []
        for document in self.documents:
            words = document.split()
            vowel_words = [word for word in words if any(char in vowels for char in word)]
            filtered_words.extend(vowel_words)
        return filtered_words

if __name__ == '__main__':
    sample_documents = [
        "Hello world, this is a test.",
        "Python programming is fun!",
        "Vowels are important in language."
    ]
    selector = VowelWordSelector(sample_documents)
    print(selector.filter_vowel_words())