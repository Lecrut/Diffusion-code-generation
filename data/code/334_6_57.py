import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1.upper()}{word2.lower()}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        self.assertEqual(combine_words("hello", "world"), "HELLOWORLD")
    def test_empty_first_word(self):
        self.assertEqual(combine_words("", "test"), "TEST")
    def test_empty_second_word(self):
        self.assertEqual(combine_words("name", ""), "NAME")
    def test_special_characters(self):
        self.assertEqual(combine_words("!@#", "$%^"), "!@#$%^")
if __name__ == '__main__':
    unittest.main(exit=False)