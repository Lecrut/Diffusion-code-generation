import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1.upper()} {word2.lower()}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        result = combine_words("hello", "world")
        self.assertEqual(result, "HELLO WORLD")
    def test_empty_strings(self):
        result = combine_words("", "")
        self.assertEqual(result, "" )
    def test_mixed_case_input(self):
        result = combine_words("Python", "Programming")
        self.assertEqual(result, "PYTHON programming")
    def test_special_characters_preserved_in_word2_lowering(self):
        result = combine_words("test", "a1b2c3")
        self.assertEqual(result, "TEST a1b2c3")
if __name__ == '__main__':
    unittest.main(exit=False)