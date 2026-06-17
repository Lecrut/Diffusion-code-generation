import unittest
def check_word_length(word, threshold):
    return len(word) > threshold
class TestWordLengthChecker(unittest.TestCase):
    def test_word_longer_than_threshold(self):
        self.assertTrue(check_word_length("testing", 4))
        self.assertTrue(check_word_length("longerword", 8))
    def test_word_shorter_than_threshold(self):
        self.assertFalse(check_word_length("short", 5))
        self.assertFalse(check_word_length("a", 2))
    def test_word_equal_to_threshold(self):
        self.assertFalse(check_word_length("hello", 5))
        self.assertFalse(check_word_length("five", 4))
    def test_empty_string(self):
        self.assertFalse(check_word_length("", 0))
        self.assertFalse(check_word_length("", 1))
    def test_various_thresholds(self):
        word = "programming"
        self.assertTrue(check_word_length(word, 8))
        self.assertFalse(check_word_length(word, 7))
        self.assertFalse(check_word_length(word, 10))
    def test_long_words(self):
        self.assertTrue(check_word_length("supercalifragilisticexpialidocious", 30))
        self.assertFalse(check_word_length("short", 50))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)