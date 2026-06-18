import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1}{word2}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        result = combine_words("hello", "world")
        self.assertEqual(result, "helloworld")
    def test_empty_string_first(self):
        result = combine_words("", "test")
        self.assertEqual(result, "test")
    def test_empty_string_second(self):
        result = combine_words("prefix", "")
        self.assertEqual(result, "prefix")
    def test_single_char_input(self):
        result = combine_words("a", "b")
        self.assertEqual(result, "ab")
if __name__ == '__main__':
    unittest.main()