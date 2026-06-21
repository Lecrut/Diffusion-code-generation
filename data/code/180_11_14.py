class WordPresenceChecker:
    def __init__(self, large_text):
        self.word_set = set(large_text.split())

    def is_word_present(self, word):
        return word in self.word_set

if __name__ == '__main__':
    sample_text = "this is a very long string designed to test the efficiency of substring searching in Python for very long texts"
    word_to_find = "long"
    checker = WordPresenceChecker(sample_text)
    result = checker.is_word_present(word_to_find)
    print(result)

    sample_text_2 = "abcdefghijklmnopqrstuvwxyz" * 10000
    word_to_find_2 = "z"
    checker_2 = WordPresenceChecker(sample_text_2)
    result_2 = checker_2.is_word_present(word_to_find_2)
    print(result_2)

    sample_text_3 = "hello world"
    word_to_find_3 = "goodbye"
    checker_3 = WordPresenceChecker(sample_text_3)
    result_3 = checker_3.is_word_present(word_to_find_3)
    print(result_3)