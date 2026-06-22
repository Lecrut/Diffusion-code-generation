class WordChecker:
    def is_long(self, word):
        return len(word) > 10

if __name__ == '__main__':
    checker = WordChecker()
    sample_word_one = "short"
    sample_word_two = "thisisalongstring"
    sample_word_three = "tenchars"
    
    print(f"'{sample_word_one}' is long: {checker.is_long(sample_word_one)}")
    print(f"'{sample_word_two}' is long: {checker.is_long(sample_word_two)}")
    print(f"'{sample_word_three}' is long: {checker.is_long(sample_word_three)}")