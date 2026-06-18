import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1}{word2}"
class TestCombineWords(unittest.TestCase):
    def test_combine_simple(self):
        self.assertEqual(combine_words("hello", "world"), "helloworld")
    def test_combine_empty_first(self):
        self.assertEqual(combine_words("", "test"), "test")
    def test_combine_empty_second(self):
        self.assertEqual(combine_words("prefix", ""), "prefix")
    def test_case_sensitivity(self):
        self.assertEqual(combine_words("A", "b"), "Ab")
if __name__ == '__main__':
    unittest.main()