import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1} {word2}"
class TestCombineWords(unittest.TestCase):
    def test_combine_simple(self):
        self.assertEqual(combine_words("hello", "world"), "hello world")
    def test_combine_with_numbers(self):
        self.assertEqual(combine_words("test", "123"), "test 123")
    def test_combine_empty_strings_raises_error(self):
        with self.assertRaises(ValueError) as context:
            combine_words("", "")
        self.assertIn("empty strings", str(context.exception))
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)