class LetterAnalyzer:
    ALPHABET = set('abcdefghijklmnopqrstuvwxyz')

    @staticmethod
    def is_alpha(char):
        return char.lower() in LetterAnalyzer.ALPHABET

    def find_repeated_letters(self, sentence):
        letter_count = {}
        repeated_letters = set()
        for char in sentence:
            if self.is_alpha(char):
                char_lower = char.lower()
                if char_lower in letter_count:
                    letter_count[char_lower] += 1
                    repeated_letters.add(char_lower)
                else:
                    letter_count[char_lower] = 1
        return repeated_letters

if __name__ == '__main__':
    sample_sentence = "This is a unique example with some repeated letters."
    analyzer = LetterAnalyzer()
    result = analyzer.find_repeated_letters(sample_sentence)
    print(result)