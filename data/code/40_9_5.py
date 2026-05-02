import unittest
def extract_first_letters(text):
    words = text.split()
    first_letters = [word[0] for word in words if word]
    return first_letters
class TestExtractFirstLetters(unittest.TestCase):
    def test_normal_string(self):
        self.assertEqual(extract_first_letters("Hello world"), ["H", "w"])
    def test_empty_string(self):
        self.assertEqual(extract_first_letters(""), [])
    def test_string_with_only_spaces(self):
        self.assertEqual(extract_first_letters("   \t "), [])
    def test_string_with_leading_and_trailing_spaces(self):
        self.assertEqual(extract_first_letters("  Test case "), ["T", "c"])
    def test_string_with_multiple_spaces(self):
        self.assertEqual(extract_first_letters("One   two   three"), ["O", "t", "t"])
    def test_string_with_punctuation_attached(self):
        self.assertEqual(extract_first_letters("Hello, world!"), ["H", "w"])
    def test_string_with_hyphenated_words(self):
        self.assertEqual(extract_first_letters("State-of-the-art"), ["S", "o", "t", "a"])
    def test_string_with_empty_words_from_splitting(self):
        self.assertEqual(extract_first_letters("Word1  Word2"), ["W", "W"])
    def test_string_with_only_punctuation(self):
        self.assertEqual(extract_first_letters("!@#$ %^&*"), [])
    def test_string_with_mixed_content(self):
        self.assertEqual(extract_first_letters("A B, C. D"), ["A", "B", "C", "D"])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)