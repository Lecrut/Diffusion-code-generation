class WordChecker:
    CHECK_WORDS = ['apple', 'banana', 'cherry']

    @staticmethod
    def is_word_present(word: str) -> bool:
        return word in WordChecker.CHECK_WORDS

if __name__ == '__main__':
    print(f"Test 1 (Present): {WordChecker.is_word_present('apple')}")
    print(f"Test 2 (Absent): {WordChecker.is_word_present('grape')}")