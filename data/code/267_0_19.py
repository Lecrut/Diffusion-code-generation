class WordChecker:
    MAX_LENGTH = 10

    @staticmethod
    def is_long(word):
        return len(word) > WordChecker.MAX_LENGTH

if __name__ == '__main__':
    sample_word_one = "short"
    sample_word_two = "thisisalongword"
    print(f"'{sample_word_one}' is long: {WordChecker.is_long(sample_word_one)}")
    print(f"'{sample_word_two}' is long: {WordChecker.is_long(sample_word_two)}")