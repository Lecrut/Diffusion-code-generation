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
        text = "This is a test sentence"
        self.assertEqual(self.counter.count_words(text), 5)
    def test_empty_string(self):
        text = ""
        self.assertEqual(self.counter.count_words(text), 0)
    def test_string_with_only_spaces(self):
        text = "   \t  "
        self.assertEqual(self.counter.count_words(text), 0)
    def test_multiple_spaces(self):
        text = "Hello   world"
        self.assertEqual(self.counter.count_words(text), 2)
    def test_leading_and_trailing_spaces(self):
        text = "  Start and end "
        self.assertEqual(self.counter.count_words(text), 3)
    def test_single_word(self):
        text = "Word"
        self.assertEqual(self.counter.count_words(text), 1)
    def test_only_punctuation(self):
        text = ".,! ? "
        self.assertEqual(self.counter.count_words(text), 0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)