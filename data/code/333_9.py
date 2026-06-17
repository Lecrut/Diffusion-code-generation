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
        self.assertEqual(extract_first_letters("  Start end "), ["S", "e"])
    def test_empty_input(self):
        self.assertEqual(extract_first_letters(""), [])
    def test_only_spaces(self):
        self.assertEqual(extract_first_letters("   \t\n "), [])
    def test_punctuation_attached(self):
        self.assertEqual(extract_first_letters("Hello, world!"), ["H", "w"])
    def test_numbers_and_symbols_as_words(self):
        self.assertEqual(extract_first_letters("Word1 Word2!"), ["W", "W"])
    def test_empty_words_due_to_multiple_delimiters(self):
        self.assertEqual(extract_first_letters("A,,B"), ["A", "B"])
    def test_long_words(self):
        self.assertEqual(extract_first_letters("Supercalifragilisticexpialidocious"), ["S"])
    def test_mixed_case(self):
        self.assertEqual(extract_first_letters("MiXeD cAsE"), ["M", "c"])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)