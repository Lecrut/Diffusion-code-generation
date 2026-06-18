import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1}_{word2}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        self.assertEqual(combine_words("hello", "world"), "hello_world")
    def test_empty_strings(self):
        self.assertEqual(combine_words("", ""), "_")
    def test_case_sensitivity(self):
        self.assertEqual(combine_words("Test", "Case"), "Test_Case")
    def test_single_character(self):
        self.assertEqual(combine_words("a", "b"), "a_b")
if __name__ == '__main__':
    unittest.main()