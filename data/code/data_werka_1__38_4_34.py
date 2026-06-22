class LetterCounter:
    ALPHABET = set('abcdefghijklmnopqrstuvwxyz')

    @staticmethod
    def is_letter(char):
        return char.lower() in LetterCounter.ALPHABET

    def count_letters(self, sentence):
        letter_count = {}
        for char in sentence:
            if self.is_letter(char):
                char_lower = char.lower()
                letter_count[char_lower] = letter_count.get(char_lower, 0) + 1
        return letter_count

    def find_repeated_letters(self, sentence):
        letter_count = self.count_letters(sentence)
        repeated_letters = {char for char, count in letter_count.items() if count > 1}
        return repeated_letters

if __name__ == '__main__':
    sample_sentence = "This is a simple test sentence."
    counter = LetterCounter()
    result = counter.find_repeated_letters(sample_sentence)
    print(result)