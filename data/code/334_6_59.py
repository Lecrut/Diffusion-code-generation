import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1}{word2}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        result = combine_words("hello", "world")
        self.assertEqual(result, "helloworld")
    def test_empty_first_word(self):
        result = combine_words("", "test")
        self.assertEqual(result, "test")
    def test_empty_second_word(self):
        result = combine_words("prefix", "")
        self.assertEqual(result, "prefix")
    def test_single_characters(self):
        result = combine_words("a", "b")
        self.assertEqual(result, "ab")
    def test_special_characters_in_input(self):
        result = combine_words("!@#", "$%^&*()")
        self.assertEqual(result, "!@$%^&*()")
if __name__ == '__main__':
    unittest.main(exit=False)