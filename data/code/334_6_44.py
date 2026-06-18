import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1} {word2}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        result = combine_words("hello", "world")
        self.assertEqual(result, "hello world")
    def test_empty_first_word(self):
        result = combine_words("", "test")
        self.assertEqual(result, " test")
    def test_empty_second_word(self):
        result = combine_words("input", "")
        self.assertEqual(result, "input ")
    def test_single_letter_words(self):
        result = combine_words("a", "b")
        self.assertEqual(result, "a b")
    def test_capitalization_preservation(self):
        result = combine_words("Python", "is")
        self.assertEqual(result, "Python is")
if __name__ == '__main__':
    unittest.main()