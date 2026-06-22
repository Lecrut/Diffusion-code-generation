class LetterCounter:
    def __init__(self, sentence):
        self.sentence = sentence
        self.letter_count = {}
    
    def count_letters(self):
        for char in self.sentence:
            if char.isalpha():
                char_lower = char.lower()
                self.letter_count[char_lower] = self.letter_count.get(char_lower, 0) + 1
    
    def find_repeated_letters(self):
        repeated_letters = {char for char, count in self.letter_count.items() if count > 1}
        return repeated_letters

if __name__ == '__main__':
    sample_sentence = "A fresh corrected module that satisfies every contract rule above."
    letter_counter = LetterCounter(sample_sentence)
    try:
        letter_counter.count_letters()
        result = letter_counter.find_repeated_letters()
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")