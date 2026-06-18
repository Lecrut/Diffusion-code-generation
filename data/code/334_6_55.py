import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1} {word2}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        self.assertEqual(combine_words("hello", "world"), "hello world")
    def test_empty_first_word(self):
        self.assertEqual(combine_words("", "test"), " test")
    def test_empty_second_word(self):
        self.assertEqual(combine_words("input", ""), "input ")
    def test_single_character(self):
        self.assertEqual(combine_words("a", "b"), "a b")
    def test_uppercase_letters(self):
        self.assertEqual(combine_words("HELLO", "WORLD"), "HELLO WORLD")
if __name__ == '__main__':
    unittest.main()