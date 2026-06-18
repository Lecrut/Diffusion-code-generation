import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1} {word2}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        result = combine_words("hello", "world")
        self.assertEqual(result, "hello world")
    def test_empty_string_input(self):
        result = combine_words("", "test")
        self.assertEqual(result, " test")
    def test_single_character_inputs(self):
        result = combine_words("a", "b")
        self.assertEqual(result, "a b")
    def test_longer_words(self):
        word1 = "this_is_a_test"
        word2 = "another_one_too"
        result = combine_words(word1, word2)
        expected = f"{word1} {word2}"
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()