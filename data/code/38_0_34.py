class RepeatedLetterFinder:
    def __init__(self, input_string):
        self.input_string = input_string.lower()
        self.seen_letters = set()
        self.repeated_letters = set()

    def find_repeated(self):
        for char in self.input_string:
            if 'a' <= char <= 'z':
                if char in self.seen_letters:
                    self.repeated_letters.add(char)
                else:
                    self.seen_letters.add(char)
        return sorted(list(self.repeated_letters))

if __name__ == '__main__':
    sample_string_1 = "programming"
    finder_1 = RepeatedLetterFinder(sample_string_1)
    print(f"Repeated letters in '{sample_string_1}':", finder_1.find_repeated())

    sample_string_2 = "hello world"
    finder_2 = RepeatedLetterFinder(sample_string_2)
    print(f"Repeated letters in '{sample_string_2}':", finder_2.find_repeated())

    sample_string_3 = "abcdefg"
    finder_3 = RepeatedLetterFinder(sample_string_3)
    print(f"Repeated letters in '{sample_string_3}':", finder_3.find_repeated())

    sample_string_4 = "aabbccddeeff"
    finder_4 = RepeatedLetterFinder(sample_string_4)
    print(f"Repeated letters in '{sample_string_4}':", finder_4.find_repeated())