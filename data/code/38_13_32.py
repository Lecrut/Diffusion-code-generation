class LetterCounter:
    def __init__(self, string):
        self.string = string

    @staticmethod
    def is_alpha(char):
        return char.isalpha()

    @staticmethod
    def to_lower(char):
        return char.lower()

    def count_repeated_letters(self):
        letter_count = {}
        for char in self.string:
            if self.is_alpha(char):
                char_lower = self.to_lower(char)
                if char_lower in letter_count:
                    letter_count[char_lower] += 1
                else:
                    letter_count[char_lower] = 1
        repeated_letters = {char: count for char, count in letter_count.items() if count > 1}
        return repeated_letters

if __name__ == '__main__':
    sample_string = 'Hello World! This is a Test String with some Repeated letters.'
    counter = LetterCounter(sample_string)
    result = counter.count_repeated_letters()
    print(result)