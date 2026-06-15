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
    large_text = "this is a very long string designed to test the efficiency of substring searching within large bodies of text. we need to ensure that this method performs well even when the input strings are extremely long and contain many repetitions."
    word_to_find = "long"
    word_not_present = "nonexistent"
    result1 = checker.contains_word_optimized(large_text, word_to_find)
    result2 = checker.contains_word_optimized(large_text, word_not_present)
    print(f"Does the text contain '{word_to_find}'? {result1}")
    print(f"Does the text contain '{word_not_present}'? {result2}")