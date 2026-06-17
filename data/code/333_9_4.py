import unittest
def extract_first_letters(text):
    words = text.split()
    first_letters = [word[0] for word in words if word]
    return first_letters
class TestExtractFirstLetters(unittest.TestCase):
    def test_standard_sentence(self):
        self.assertEqual(extract_first_letters("Hello world this is a test"), ["H", "w", "t", "i", "a", "t"])
    def test_single_word(self):
        self.assertEqual(extract_first_letters("SingleWord"), ["S"])
    def test_empty_string(self):
        self.assertEqual(extract_first_letters(""), [])
    def test_multiple_spaces(self):
        self.assertEqual(extract_first_letters("  leading space   and multiple  spaces"), ["l", "a", "s"])
    def test_punctuation_attached(self):
        self.assertEqual(extract_first_letters("Hello, world! How are you?"), ["H", "w", "H", "a", "y"])
    def test_empty_words_from_multiple_spaces(self):
        self.assertEqual(extract_first_letters("word1  word2   word3"), ["w", "w", "w"])
    def test_only_spaces(self):
        self.assertEqual(extract_first_letters("     \t\n "), [])
    def test_empty_input(self):
        self.assertEqual(extract_first_letters(""), [])
    def test_text_with_numbers(self):
        self.assertEqual(extract_first_letters("Word1 Word2 3rd"), ["W", "W", "3"])
    def test_long_words(self):
        self.assertEqual(extract_first_letters("Supercalifragilisticexpialidocious"), ["S"])
    def test_mixed_case(self):
        self.assertEqual(extract_first_letters("tHis Is A TeSt"), ["t", "I", "A", "T"])
    def test_only_punctuation(self):
        self.assertEqual(extract_first_letters("!@#$%^&*()"), [])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)