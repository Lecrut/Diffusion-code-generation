import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1}{word2}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        self.assertEqual(combine_words("hello", "world"), "helloworld")
    def test_empty_first_word(self):
        self.assertEqual(combine_words("", "test"), "test")
    def test_empty_second_word(self):
        self.assertEqual(combine_words("start", ""), "start")
    def test_single_characters(self):
        self.assertEqual(combine_words("a", "b"), "ab")
    def test_special_chars_in_input(self):
        self.assertEqual(combine_words("!@#", "$%^&*"), "!@$%^&*")
if __name__ == '__main__':
    unittest.main(exit=False)