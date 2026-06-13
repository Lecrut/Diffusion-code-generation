class StringChecker:
    def __init__(self):
        pass
    def contains_word_optimized(self, text: str, word: str) -> bool:
        if not word:
            return True
        if not text:
            return False
        return word in text
if __name__ == '__main__':
    checker = StringChecker()
    large_text = "this is a very long string designed to test the efficiency of substring searching algorithms for very large texts and we need to ensure that this operation is as fast as possible"
    word_to_find = "long"
    word_not_found = "nonexistent"
    empty_word = ""
    result1 = checker.contains_word_optimized(large_text, word_to_find)
    result2 = checker.contains_word_optimized(large_text, word_not_found)
    result3 = checker.contains_word_optimized(large_text, empty_word)
    print(f"Does '{word_to_find}' exist in the text? {result1}")
    print(f"Does '{word_not_found}' exist in the text? {result2}")
    print(f"Does the empty string exist in the text? {result3}")