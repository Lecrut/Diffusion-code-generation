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
    large_text = "this is a very long string designed to test the efficiency of substring searching algorithms for very long texts"
    word_to_find = "long"
    print(checker.contains_word_optimized(large_text, word_to_find))
    large_text_2 = "this is another very long text example"
    word_to_find_2 = "example"
    print(checker.contains_word_optimized(large_text_2, word_to_find_2))
    large_text_3 = "short text"
    word_to_find_3 = "verylong"
    print(checker.contains_word_optimized(large_text_3, word_to_find_3))