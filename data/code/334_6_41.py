import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1} {word2}"
class TestCombineWords(unittest.TestCase):
    def test_combine_simple(self):
        self.assertEqual(combine_words("hello", "world"), "hello world")
    def test_combine_with_spaces_in_word(self):
        self.assertEqual(combine_words("python", "programming"), "python programming")
    def test_case_sensitivity_preserved(self):
        result = combine_words("Hello", "WORLD")
        self.assertEqual(result, "Hello WORLD")
if __name__ == '__main__':
    unittest.main()