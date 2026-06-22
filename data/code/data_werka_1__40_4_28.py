class LetterExtractor:
    def __init__(self, input_string):
        self.input_string = input_string

    def find_first_letters(self):
        words = self.input_string.split()
        for word in words:
            if word:
                yield word[0]

if __name__ == '__main__':
    test_cases = [
        "This is a sample string",
        "  leading spaces and multiple    spaces ",
        "",
        "singleword"
    ]

    for i, test_string in enumerate(test_cases, start=1):
        print(f"\nTest {i}:")
        extractor = LetterExtractor(test_string)
        for letter in extractor.find_first_letters():
            print(letter)