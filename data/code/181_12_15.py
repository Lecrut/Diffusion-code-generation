class VowelWordIdentifier:
    def __init__(self):
        self.vowels = set('aeiou')

    def identify_vowel_words(self, text):
        words = text.lower().split()
        return {word for word in words if any(char in self.vowels for char in word)}

if __name__ == '__main__':
    identifier = VowelWordIdentifier()
    sample_text = "This is a test sentence with many words including apple and banana."
    vowel_words = identifier.identify_vowel_words(sample_text)
    print(vowel_words)