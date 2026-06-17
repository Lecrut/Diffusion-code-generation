import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1} {word2}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        self.assertEqual(combine_words("hello", "world"), "hello world")
    def test_empty_first_word(self):
        self.assertEqual(combine_words("", "test"), " test")
    def test_empty_second_word(self):
        self.assertEqual(combine_words("start", ""), " start ")
    def test_special_characters(self):
        self.assertEqual(combine_words("!@#", "$%^&*()_+-=[]{}|;:,.<>?`~"), "!@# $%^&*()_+-=[]{}|;:,.<>?`~")
    def test_case_sensitivity_preserved(self):
        self.assertEqual(combine_words("Python", "3.10"), "Python 3.10")
if __name__ == '__main__':
    unittest.main(exit=False)