import unittest
class WordReverser:
    def reverse_words(self, text):
        words = text.split()
        words.reverse()
        return " ".join(words)
class TestWordReverser(unittest.TestCase):
    def setUp(self):
        self.reverser = WordReverser()
    def test_normal_case(self):
        self.assertEqual(self.reverser.reverse_words("hello world"), "world hello")
    def test_multiple_spaces(self):
        self.assertEqual(self.reverser.reverse_words("  the quick brown fox  "), "fox brown quick the")
    def test_empty_string(self):
        self.assertEqual(self.reverser.reverse_words(""), "")
    def test_single_word(self):
        self.assertEqual(self.reverser.reverse_words("single"), "single")
    def test_already_reversed(self):
        self.assertEqual(self.reverser.reverse_words("test word"), "word test")
    def test_leading_trailing_spaces(self):
        self.assertEqual(self.reverser.reverse_words("  start end  "), "end start")
    def test_only_spaces(self):
        self.assertEqual(self.reverser.reverse_words("   \t "), "")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)