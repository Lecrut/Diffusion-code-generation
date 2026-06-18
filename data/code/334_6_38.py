import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1}-{word2}" if len(word1) > 3 else f"{word1}{word2.capitalize()}"
class TestCombineWords(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(combine_words("hello", "world"), "hello-world")
    def test_short_first_word(self):
        self.assertEqual(combine_words("hi", "there"), "hither")
    def test_empty_string(self):
        with self.assertRaises(ValueError) as context:
            combine_words("", "")
        self.assertIn("empty string", str(context.exception))
    def test_unicode_support(self):
        result = combine_words("café", "naïve")
        self.assertEqual(result, "caf-naive")
if __name__ == '__main__':
    unittest.main(exit=False)