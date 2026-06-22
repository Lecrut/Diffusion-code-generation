class FirstLetterExtractor:
    def __init__(self, input_string):
        self.input_string = input_string

    def _split_into_words(self):
        return self.input_string.split()

    def get_first_letters(self):
        for word in self._split_into_words():
            if word:
                yield word[0]

if __name__ == '__main__':
    test_string_1 = "This is a sample string"
    extractor_1 = FirstLetterExtractor(test_string_1)
    print("Test 1:")
    for letter in extractor_1.get_first_letters():
        print(letter)

    test_string_2 = "  leading spaces and multiple    spaces "
    extractor_2 = FirstLetterExtractor(test_string_2)
    print("\nTest 2:")
    for letter in extractor_2.get_first_letters():
        print(letter)

    test_string_3 = ""
    extractor_3 = FirstLetterExtractor(test_string_3)
    print("\nTest 3:")
    for letter in extractor_3.get_first_letters():
        print(letter)