class WordLengthChecker:
    MIN_LENGTH = 15

    @staticmethod
    def is_word_long(word):
        return len(word) > WordLengthChecker.MIN_LENGTH

if __name__ == '__main__':
    print(WordLengthChecker.is_word_long("short"))
    print(WordLengthChecker.is_word_long("thisisalongword"))
    print(WordLengthChecker.is_word_long("a_very_long_string_example"))
    print(WordLengthChecker.is_word_long("exactlyfifteen"))
    print(WordLengthChecker.is_word_long(""))