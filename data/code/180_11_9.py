class StringChecker:
    def __init__(self):
        pass
    def contains_word_optimized(self, text, word):
        if not word:
            return True
        if not text:
            return False
        return word in text
if __name__ == '__main__':
    checker = StringChecker()
    large_text = "this is a very long string designed to test the efficiency of substring searching algorithms for very long texts. we need to ensure that this method performs well when the input strings are extremely large and complex."
    word_to_find = "long"
    result = checker.contains_word_optimized(large_text, word_to_find)
    print(f"Does '{word_to_find}' exist in the text? {result}")
    large_text_2 = "this is another very long string for testing purposes."
    word_to_find_2 = "testing"
    result_2 = checker.contains_word_optimized(large_text_2, word_to_find_2)
    print(f"Does '{word_to_find_2}' exist in the second text? {result_2}")
    large_text_3 = "short text."
    word_to_find_3 = "verylong"
    result_3 = checker.contains_word_optimized(large_text_3, word_to_find_3)
    print(f"Does '{word_to_find_3}' exist in the third text? {result_3}")