import unittest
def extract_first_letters(text):
    words = text.split()
    first_letters = [word[0] for word in words if word]
    return first_letters
class TestExtractFirstLetters(unittest.TestCase):
    def test_standard_sentence(self):
        self.assertEqual(extract_first_letters("Hello world this is a test"), ["H", "w", "t", "i", "a", "t"])
    def test_empty_string(self):
        self.assertEqual(extract_first_letters(""), [])
    def test_single_word(self):
        self.assertEqual(extract_first_letters("Word"), ["W"])
    def test_multiple_spaces(self):
        self.assertEqual(extract_first_letters("One   two    three"), ["O", "t", "t"])
    def test_leading_and_trailing_spaces(self):
        self.assertEqual(extract_first_letters("  Start and end "), ["S", "a", "e"])
    def test_empty_words_or_punctuation_handling(self):
        self.assertEqual(extract_first_letters("Test, one. two!"), ["T", "o", "t"])
        self.assertEqual(extract_first_letters("Word1 Word2"), ["W", "W"])
    def test_all_uppercase(self):
        self.assertEqual(extract_first_letters("PYTHON IS FUN"), ["P", "I", "F"])
    def test_numbers_as_words(self):
        self.assertEqual(extract_first_letters("Word1 Word2 3rd"), ["W", "W", "3"])
    def test_only_spaces(self):
        self.assertEqual(extract_first_letters("   \t  "), [])
    def test_complex_mixed_case(self):
        self.assertEqual(extract_first_letters("aBc DeFg HiJ"), ["a", "D", "H"])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)