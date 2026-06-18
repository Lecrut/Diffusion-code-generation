import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1}{word2}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        self.assertEqual(combine_words("hello", "world"), "helloworld")
    def test_empty_string_handling(self):
        self.assertEqual(combine_words("", "test"), "test")
        self.assertEqual(combine_words("pre", ""), "pre")
    def test_special_characters(self):
        result = combine_words("!@#", "$%^&*()")
        expected = "!@$%^&*()"
        self.assertEqual(result, expected)
    def test_case_sensitivity_preservation(self):
        self.assertEqual(combine_words("A", "b"), "Ab")
if __name__ == '__main__':
    unittest.main(exit=False)