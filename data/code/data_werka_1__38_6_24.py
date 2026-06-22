class LetterFrequencyAnalyzer:
    ALPHABET = set('abcdefghijklmnopqrstuvwxyz')

    @staticmethod
    def is_valid_letter(char):
        return char in LetterFrequencyAnalyzer.ALPHABET

    def analyze(self, text):
        frequency = {}
        for char in text.lower():
            if self.is_valid_letter(char):
                frequency[char] = frequency.get(char, 0) + 1
        frequent_letters = {letter: count for letter, count in frequency.items() if count > 1}
        return frequent_letters

if __name__ == '__main__':
    sample_string = "Hello World! This is a test string."
    analyzer = LetterFrequencyAnalyzer()
    result = analyzer.analyze(sample_string)
    print(result)