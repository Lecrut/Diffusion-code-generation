class LetterCounter:
    def __init__(self):
        self.letter_count = {}

    def add_letter(self, char):
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in self.letter_count:
                self.letter_count[char_lower] += 1
            else:
                self.letter_count[char_lower] = 1

    def find_repeated_letters(self):
        return {char for char, count in self.letter_count.items() if count > 1}

if __name__ == '__main__':
    sample_string_1 = "programming"
    counter_1 = LetterCounter()
    for char in sample_string_1:
        counter_1.add_letter(char)
    repeated_letters_1 = counter_1.find_repeated_letters()
    print("Repeated letters in", sample_string_1, ":", repeated_letters_1)

    sample_string_2 = "hello world"
    counter_2 = LetterCounter()
    for char in sample_string_2:
        counter_2.add_letter(char)
    repeated_letters_2 = counter_2.find_repeated_letters()
    print("Repeated letters in", sample_string_2, ":", repeated_letters_2)

    sample_string_3 = "banana"
    counter_3 = LetterCounter()
    for char in sample_string_3:
        counter_3.add_letter(char)
    repeated_letters_3 = counter_3.find_repeated_letters()
    print("Repeated letters in", sample_string_3, ":", repeated_letters_3)