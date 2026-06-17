import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1} {word2}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        self.assertEqual(combine_words("hello", "world"), "hello world")
    def test_empty_string_handling(self):
        self.assertEqual(combine_words("", "test"), " test")
        self.assertEqual(combine_words("prefix", ""), "prefix ")
    def test_single_character_words(self):
        self.assertEqual(combine_words("a", "b"), "a b")
    def test_special_characters_in_word1(self):
        self.assertEqual(combine_words("!@#", "$%^"), "!@# $%^")
if __name__ == '__main__':
    unittest.main()