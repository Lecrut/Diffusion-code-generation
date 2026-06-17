import unittest
def extract_first_letters(text):
    words = text.split()
    first_letters = [word[0] for word in words if word]
    return first_letters
class TestExtractFirstLetters(unittest.TestCase):
    def test_standard_sentence(self):
        self.assertEqual(extract_first_letters("Hello world this is a test"), ["H", "w", "t", "i", "a", "t"])
    def test_single_word(self):
        self.assertEqual(extract_first_letters("Singleword"), ["S"])
    def test_empty_string(self):
        self.assertEqual(extract_first_letters(""), [])
    def test_multiple_spaces(self):
        self.assertEqual(extract_first_letters("  leading space   and multiple  spaces"), ["a", "m", "s"])
    def test_punctuation_attached(self):
        self.assertEqual(extract_first_letters("Hello, world! How are you?"), ["H", "w", "H", "a", "y"])
    def test_empty_words_from_multiple_spaces(self):
        self.assertEqual(extract_first_letters("word1  word2   "), ["w", "w"])
    def test_numbers_and_symbols_as_words(self):
        self.assertEqual(extract_first_letters("Word1 Word2 3rd item"), ["W", "W", "3rd"])
    def test_leading_and_trailing_spaces(self):
        self.assertEqual(extract_first_letters("  start and end  "), ["s", "a", "e"])
    def test_only_spaces(self):
        self.assertEqual(extract_first_letters("     "), [])
    def test_empty_input(self):
        self.assertEqual(extract_first_letters(""), [])
    def test_long_words(self):
        self.assertEqual(extract_first_letters("Supercalifragilisticexpialidocious example"), ["S", "e"])
    def test_mixed_case(self):
        self.assertEqual(extract_first_letters("tHis Is A Test"), ["t", "I", "A", "T"])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)