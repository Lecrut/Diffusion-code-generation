import unittest
def extract_first_letters(text):
    words = text.split()
    first_letters = [word[0] for word in words if word]
    return first_letters
class TestFirstLetterExtractor(unittest.TestCase):
    def test_basic_sentence(self):
        self.assertEqual(extract_first_letters("Hello world"), ["H", "w"])
    def test_multiple_words(self):
        self.assertEqual(extract_first_letters("This is a test sentence"), ["T", "i", "a", "t", "s"])
    def test_empty_string(self):
        self.assertEqual(extract_first_letters(""), [])
    def test_single_word(self):
        self.assertEqual(extract_first_letters("Word"), ["W"])
    def test_leading_and_trailing_spaces(self):
        self.assertEqual(extract_first_letters("  Spaces around words "), ["S", "a", "w"])
    def test_multiple_spaces(self):
        self.assertEqual(extract_first_letters("Word1   Word2    Word3"), ["W", "W", "W"])
    def test_punctuation_attached(self):
        self.assertEqual(extract_first_letters("Hello, world!"), ["H", "w"])
    def test_empty_words_from_multiple_spaces(self):
        self.assertEqual(extract_first_letters("Word1  Word2"), ["W", "W"])
    def test_only_spaces(self):
        self.assertEqual(extract_first_letters("   \t\n "), [])
    def test_numbers_as_words(self):
        self.assertEqual(extract_first_letters("Word1 Word2"), ["W", "W"])
    def test_long_words(self):
        self.assertEqual(extract_first_letters("Supercalifragilisticexpialidocious"), ["S"])
    def test_mixed_case(self):
        self.assertEqual(extract_first_letters("aBc DeFg"), ["a", "D"])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)