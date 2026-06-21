class WordValidator:
    def __init__(self, words):
        self.words_set = set(words)

    def is_word_present(self, word):
        return word in self.words_set

if __name__ == '__main__':
    validator = WordValidator(['apple', 'banana', 'cherry'])
    print(f"Test 1 (Present): {validator.is_word_present('banana')}")
    print(f"Test 2 (Absent): {validator.is_word_present('grape')}")