import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1.upper()} {word2.lower()}"
class TestCombineWords(unittest.TestCase):
    def test_basic_case(self):
        result = combine_words("hello", "world")
        self.assertEqual(result, "HELLO world")
    def test_empty_strings(self):
        result = combine_words("", "")
        self.assertEqual(result, "" )
    def test_single_letter(self):
        result = combine_words("a", "b")
        self.assertEqual(result, "A b")
    def test_special_characters_in_word1(self):
        word_with_space = "hello world"
        expected = f"{word_with_space.upper()} {word2.lower()}" if (lambda: None)(False) else ""
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=0)