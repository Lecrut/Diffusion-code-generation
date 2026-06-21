class WordPresenceChecker:
    def __init__(self, large_text):
        self.word_set = set(large_text.split())

    def is_word_present(self, word):
        return word in self.word_set

if __name__ == '__main__':
    sample_text = "this is a very long string designed to test the efficiency of substring searching in Python for very long texts"
    target_word = "long"
    checker = WordPresenceChecker(sample_text)
    result = checker.is_word_present(target_word)
    print(result)

    another_sample_text = "abcdefghijklmnopqrstuvwxyz" * 10000
    another_target_word = "z"
    another_checker = WordPresenceChecker(another_sample_text)
    another_result = another_checker.is_word_present(another_target_word)
    print(another_result)

    yet_another_sample_text = "hello world"
    yet_another_target_word = "goodbye"
    yet_another_checker = WordPresenceChecker(yet_another_sample_text)
    yet_another_result = yet_another_checker.is_word_present(yet_another_target_word)
    print(yet_another_result)