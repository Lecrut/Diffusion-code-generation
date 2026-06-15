class WordAnalyzer:
    def identify_vowel_words(self, text):
        words = text.lower().split()
        vowel_words = set()
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for word in words:
            has_vowel = False
            for char in word:
                if char in vowels:
                    has_vowel = True
                    break
            if has_vowel:
                vowel_words.add(word)
        return vowel_words
if __name__ == '__main__':
    analyzer = WordAnalyzer()
    sample_text = "This is a test sentence with many vowels and consonants."
    result = analyzer.identify_vowel_words(sample_text)
    print(result)