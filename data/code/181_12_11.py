class WordAnalyzer:
    def __init__(self):
        self.vowels = {'a', 'e', 'i', 'o', 'u'}

    def identify_vowel_words(self, text):
        return {word for word in text.lower().split() if any(char in self.vowels for char in word)}

if __name__ == '__main__':
    analyzer = WordAnalyzer()
    sample_text1 = "This is a sample sentence with many words including apple and banana."
    print(analyzer.identify_vowel_words(sample_text1))
    
    sample_text2 = "This is a test sentence with many words and some consonants like r and t."
    print(analyzer.identify_vowel_words(sample_text2))