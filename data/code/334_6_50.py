import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1}_{word2}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        result = combine_words("hello", "world")
        self.assertEqual(result, "hello_world")
    def test_empty_first_word(self):
        result = combine_words("", "test")
        self.assertEqual(result, "_test")
    def test_empty_second_word(self):
        result = combine_words("input", "")
        self.assertEqual(result, "input_")
    def test_special_characters_in_words(self):
        result = combine_words("a-b", "c-d")
        self.assertEqual(result, "a-b_c-d")
if __name__ == '__main__':
    unittest.main()