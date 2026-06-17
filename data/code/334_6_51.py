import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1}-{word2}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        self.assertEqual(combine_words("hello", "world"), "hello-world")
    def test_empty_string_first(self):
        self.assertEqual(combine_words("", "test"), "-test")
    def test_empty_string_second(self):
        self.assertEqual(combine_words("prefix", ""), "prefix-")
    def test_uppercase_handling(self):
        self.assertEqual(combine_words("Python", "Programming"), "Python-Programming")
if __name__ == '__main__':
    unittest.main()