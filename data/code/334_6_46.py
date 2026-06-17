import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1}-{word2[::-1]}"
class TestCombineWords(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(combine_words("hello", "world"), "hello-dlrow")
    def test_empty_string_second_word(self):
        self.assertEqual(combine_words("test", ""), "test-")
    def test_uppercase_input(self):
        self.assertEqual(combine_words("Python", "Code"), "Python-edoC")
    def test_single_character_words(self):
        self.assertEqual(combine_words("a", "b"), "a-b")
if __name__ == '__main__':
    unittest.main()