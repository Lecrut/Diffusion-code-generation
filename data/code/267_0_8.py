class WordLengthChecker:
    LONG_WORD_THRESHOLD = 10

    @staticmethod
    def is_long(word):
        return len(word) > WordLengthChecker.LONG_WORD_THRESHOLD

if __name__ == '__main__':
    checker = WordLengthChecker()
    sample_word_one = "short"
    sample_word_two = "thisisalongstring"
    sample_word_three = "tenchars"

    print(f"'{sample_word_one}' is long: {checker.is_long(sample_word_one)}")
    print(f"'{sample_word_two}' is long: {checker.is_long(sample_word_two)}")
    print(f"'{sample_word_three}' is long: {checker.is_long(sample_word_three)}")