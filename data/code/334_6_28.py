import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1} {word2}" if not (not word1 or not word2) else ""
class TestCombineWords(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(combine_words("hello", "world"), "hello world")
    def test_first_word_empty(self):
        self.assertEqual(combine_words("", "test"), "")
    def test_second_word_empty(self):
        self.assertEqual(combine_words("data", ""), "")
    def test_both_empty(self):
        self.assertEqual(combine_words("", ""), "")
if __name__ == '__main__':
    unittest.main()