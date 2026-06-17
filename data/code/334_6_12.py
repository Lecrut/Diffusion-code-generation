import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1.upper()}{word2.lower()}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        self.assertEqual(combine_words("hello", "world"), "HELLOWORLD")
    def test_empty_first_word(self):
        self.assertEqual(combine_words("", "test"), "TEST")
    def test_empty_second_word(self):
        self.assertEqual(combine_words("input", ""), "INPUT")
    def test_special_characters_in_input(self):
        result = combine_words("!@#", "$%^&*()")
        expected = "!@#$%^&*()"
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main(exit=False)