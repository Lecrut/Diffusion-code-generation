import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1}{word2}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        self.assertEqual(combine_words("hello", "world"), "helloworld")
    def test_empty_first_word(self):
        self.assertEqual(combine_words("", "test"), "test")
    def test_empty_second_word(self):
        self.assertEqual(combine_words("prefix", ""), "prefix")
    def test_case_sensitivity(self):
        self.assertEqual(combine_words("A", "b"), "Ab")
    def test_special_characters_in_input(self):
        self.assertEqual(combine_words("!@#", "$%^&*()"), "!@$%^&()*")
if __name__ == '__main__':
    unittest.main(exit=False)