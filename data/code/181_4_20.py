class VowelWordSelector:
    def __init__(self, texts):
        self.texts = texts

    def select_vowel_words(self):
        vowels = "aeiouAEIOU"
        selected_words = []
        for text in self.texts:
            words = text.split()
            vowel_words = [word for word in words if any(char in vowels for char in word)]
            selected_words.extend(vowel_words)
        return selected_words

if __name__ == '__main__':
    sample_texts = [
        "Python is an interpreted, high-level and general-purpose programming language.",
        "Vowels are essential for forming words in most languages."
    ]
    selector = VowelWordSelector(sample_texts)
    print(selector.select_vowel_words())