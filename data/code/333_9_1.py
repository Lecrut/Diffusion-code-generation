import unittest
def extract_first_letters(text):
    words = text.split()
    first_letters = [word[0] for word in words if word]
    return first_letters
class TestFirstLetterExtractor(unittest.TestCase):
    def test_standard_sentence(self):
        self.assertEqual(extract_first_letters("Hello world this is a test"), ["H", "w", "t", "i", "a", "t"])
    def test_single_word(self):
        self.assertEqual(extract_first_letters("Singleword"), ["S"])
    def test_empty_string(self):
        self.assertEqual(extract_first_letters(""), [])
    def test_multiple_spaces(self):
        self.assertEqual(extract_first_letters("  leading and   multiple spaces "), ["l", "a", "m", "s"])
    def test_punctuation_attached(self):
        self.assertEqual(extract_first_letters("Hello, world! This is fine."), ["H", "w", "T", "i", "f"])
    def test_empty_words_from_multiple_spaces(self):
        self.assertEqual(extract_first_letters("word1  word2"), ["w", "w"])
    def test_only_spaces(self):
        self.assertEqual(extract_first_letters("   \t\n "), [])
    def test_numbers_and_symbols_as_words(self):
        self.assertEqual(extract_first_letters("1two three!"), ["1", "t", "t"])
        self.assertEqual(extract_first_letters("$money is here"), ["$", "m", "i", "h"])
    def test_long_words(self):
        self.assertEqual(extract_first_letters("Supercalifragilisticexpialidocious example"), ["S", "e"])
    def test_mixed_case(self):
        self.assertEqual(extract_first_letters("HeLlO wOrLd"), ["H", "w"])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)