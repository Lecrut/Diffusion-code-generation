class LetterCounter:
    def __init__(self):
        self.letter_counts = {}

    def count_letters(self, text):
        for char in text:
            if 'a' <= char <= 'z':
                self.letter_counts[char] = self.letter_counts.get(char, 0) + 1
            elif 'A' <= char <= 'Z':
                self.letter_counts[char.lower()] = self.letter_counts.get(char.lower(), 0) + 1

    def find_repeated_letters(self):
        repeated_letters = set()
        for letter, count in self.letter_counts.items():
            if count > 1:
                repeated_letters.add(letter)
        return repeated_letters

if __name__ == '__main__':
    test_string_1 = "hello world"
    counter_1 = LetterCounter()
    counter_1.count_letters(test_string_1)
    print(f"Input: '{test_string_1}', Repeated Letters: {counter_1.find_repeated_letters()}")

    test_string_2 = "programming"
    counter_2 = LetterCounter()
    counter_2.count_letters(test_string_2)
    print(f"Input: '{test_string_2}', Repeated Letters: {counter_2.find_repeated_letters()}")

    test_string_3 = "abcde"
    counter_3 = LetterCounter()
    counter_3.count_letters(test_string_3)
    print(f"Input: '{test_string_3}', Repeated Letters: {counter_3.find_repeated_letters()}")