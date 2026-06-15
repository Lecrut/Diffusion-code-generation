class StringChecker:
    def __init__(self):
        pass
    def contains_word(self, text, word):
        if not word:
            return True
        if not text:
            return False
        return word in text
if __name__ == '__main__':
    checker = StringChecker()
    large_text = "this is a very long string designed to test the efficiency of substring searching within large bodies of text. we need to ensure that this method performs well even when the input strings are extremely long and complex."
    word_to_find = "long"
    result = checker.contains_word(large_text, word_to_find)
    print(f"Does '{word_to_find}' exist in the text? {result}")
    large_text_2 = "abcdefghijklmnopqrstuvwxyz"
    word_to_find_2 = "xyz"
    result_2 = checker.contains_word(large_text_2, word_to_find_2)
    print(f"Does '{word_to_find_2}' exist in the text? {result_2}")
    empty_text = ""
    word_to_find_3 = "test"
    result_3 = checker.contains_word(empty_text, word_to_find_3)
    print(f"Does '{word_to_find_3}' exist in an empty string? {result_3}")
    empty_word = ""
    large_text_4 = "some text"
    result_4 = checker.contains_word(large_text_4, empty_word)
    print(f"Does an empty word exist in the text? {result_4}")