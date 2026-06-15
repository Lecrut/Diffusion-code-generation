class StringChecker:
    def __init__(self, text):
        self.text = text
    def contains_word(self, word):
        return word in self.text
if __name__ == '__main__':
    large_text = "this is a very long string designed to test the efficiency of substring searching in Python for very long texts we need to ensure that this method performs well regardless of the input size"
    word_to_find = "long"
    checker = StringChecker(large_text)
    result = checker.contains_word(word_to_find)
    print(result)
    large_text_2 = "abcdefghijklmnopqrstuvwxyz" * 10000
    word_to_find_2 = "z"
    checker_2 = StringChecker(large_text_2)
    result_2 = checker_2.contains_word(word_to_find_2)
    print(result_2)
    large_text_3 = "hello world"
    word_to_find_3 = "goodbye"
    checker_3 = StringChecker(large_text_3)
    result_3 = checker_3.contains_word(word_to_find_3)
    print(result_3)