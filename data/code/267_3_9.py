class WordLengthChecker:
    MIN_LENGTH = 6

    @staticmethod
    def is_word_long(word):
        return len(word) > WordLengthChecker.MIN_LENGTH

if __name__ == '__main__':
    print(WordLengthChecker.is_word_long("example"))
    print(WordLengthChecker.is_word_long("hi"))