import unittest
class WordCounter:
    def count_words(self, text):
        if not text:
            return 0
        words = text.split()
        return len(words)
class TestWordCounter(unittest.TestCase):
    def setUp(self):
        self.counter = WordCounter()
    def test_basic_sentence(self):
        self.assertEqual(self.counter.count_words("Hello world"), 2)
    def test_multiple_spaces(self):
        self.assertEqual(self.counter.count_words("Hello   world"), 2)
    def test_leading_and_trailing_spaces(self):
        self.assertEqual(self.counter.count_words("  Hello world  "), 2)
    def test_empty_string(self):
        self.assertEqual(self.counter.count_words(""), 0)
    def test_only_spaces(self):
        self.assertEqual(self.counter.count_words("   \t\n "), 0)
    def test_single_word(self):
        self.assertEqual(self.counter.count_words("Single"), 1)
    def test_punctuation_attached(self):
        self.assertEqual(self.counter.count_words("Hello, world!"), 2)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)