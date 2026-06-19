class LetterAnalyzer:
    @staticmethod
    def find_repeated_letters(sentence):
        letter_count = {}
        repeated_letters = set()
        for char in sentence:
            if char.isalpha():
                char_lower = char.lower()
                if char_lower in letter_count:
                    letter_count[char_lower] += 1
                    repeated_letters.add(char_lower)
                else:
                    letter_count[char_lower] = 1
        return repeated_letters

if __name__ == '__main__':
    sample_sentence = "This is a unique example sentence."
    analyzer = LetterAnalyzer()
    result = analyzer.find_repeated_letters(sample_sentence)
    print(result)