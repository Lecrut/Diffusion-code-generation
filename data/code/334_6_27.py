import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1} {word2}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        self.assertEqual(combine_words("hello", "world"), "hello world")
    def test_single_word_input(self):
        result = combine_words("", "test")
        self.assertEqual(result, " test")
    def test_case_sensitivity_preserved(self):
        self.assertEqual(combine_words("Hello", "World"), "Hello World")
    def test_multiple_spaces_handling(self):
        self.assertEqual(combine_words("a", "b"), "a b")
    def test_empty_string_input(self):
        result = combine_words("", "")
        self.assertEqual(result, " ")
if __name__ == '__main__':
    unittest.main()