class LetterCounter:
    def __init__(self, sentence):
        self.sentence = sentence
        self.letter_count = {}
        self.repeated_letters = set()
        self._count_letters()

    def _count_letters(self):
        for char in self.sentence:
            if char.isalpha():
                char_lower = char.lower()
                if char_lower in self.letter_count:
                    self.letter_count[char_lower] += 1
                    self.repeated_letters.add(char_lower)
                else:
                    self.letter_count[char_lower] = 1

    def get_repeated_letters(self):
        return self.repeated_letters

if __name__ == '__main__':
    sample_sentence1 = "This is a simple test sentence."
    letter_counter1 = LetterCounter(sample_sentence1)
    print(letter_counter1.get_repeated_letters())

    sample_sentence2 = "Another example with different letters."
    letter_counter2 = LetterCounter(sample_sentence2)
    print(letter_counter2.get_repeated_letters())