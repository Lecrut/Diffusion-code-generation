class StringChecker:
    def __init__(self, large_text):
        self.large_text = large_text
    def is_present(self, word):
        return word in self.large_text
if __name__ == '__main__':
    sample_text = "this is a very long string designed to test the efficiency of substring searching in Python for very long texts"
    word_to_find = "long"
    checker = StringChecker(sample_text)
    result = checker.is_present(word_to_find)
    print(result)
    sample_text_2 = "abcdefghijklmnopqrstuvwxyz" * 10000
    word_to_find_2 = "xyz"
    checker_2 = StringChecker(sample_text_2)
    result_2 = checker_2.is_present(word_to_find_2)
    print(result_2)