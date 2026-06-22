class WordLengthChecker:
    def __init__(self, min_length=15):
        self.min_length = min_length

    def is_word_long(self, s):
        return len(s) > self.min_length

if __name__ == '__main__':
    checker = WordLengthChecker()
    print(checker.is_word_long("short"))
    print(checker.is_word_long("thisisalongword"))
    print(checker.is_word_long("a_very_long_string_example"))
    print(checker.is_word_long("exactlyfifteen"))
    print(checker.is_word_long(""))