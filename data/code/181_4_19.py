VOWELS = "aeiouAEIOU"

class VowelWordSelector:
    def __init__(self, documents):
        self.documents = documents

    def select_vowel_words(self):
        vowel_words = []
        for doc in self.documents:
            words = doc.split()
            selected_words = [word for word in words if any(char in VOWELS for char in word)]
            vowel_words.extend(selected_words)
        return vowel_words

if __name__ == '__main__':
    documents = [
        "This is a test document.",
        "Another example with some vowels."
    ]
    selector = VowelWordSelector(documents)
    print(selector.select_vowel_words())