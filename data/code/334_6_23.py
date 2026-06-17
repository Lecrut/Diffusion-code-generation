import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1}-{word2}"
class TestCombineWords(unittest.TestCase):
    def test_combine_simple(self):
        self.assertEqual(combine_words("hello", "world"), "hello-world")
    def test_combine_empty_first(self):
        self.assertEqual(combine_words("", "test"), "-test")
    def test_combine_empty_second(self):
        self.assertEqual(combine_words("input", ""), "input-")
    def test_case_sensitivity(self):
        self.assertEqual(combine_words("Python", "Code"), "Python-Code")
if __name__ == '__main__':
    unittest.main()