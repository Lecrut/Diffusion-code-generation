import unittest
def extract_first_letters(text):
    words = text.split()
    first_letters = [word[0] for word in words if word]
    return first_letters
class TestExtractFirstLetters(unittest.TestCase):
    def test_normal_sentence(self):
        self.assertEqual(extract_first_letters("Hello world"), ["H", "w"])
    def test_multiple_words(self):
        self.assertEqual(extract_first_letters("This is a test string"), ["T", "i", "a", "t", "s"])
    def test_empty_string(self):
        self.assertEqual(extract_first_letters(""), [])
    def test_string_with_only_spaces(self):
        self.assertEqual(extract_first_letters("   \t\n"), [])
    def test_string_with_leading_and_trailing_spaces(self):
        self.assertEqual(extract_first_letters("  leading and trailing  "), ["l", "a", "t"])
    def test_string_with_punctuation(self):
        self.assertEqual(extract_first_letters("Hello, world!"), ["H", "w"])
    def test_string_with_mixed_punctuation_and_numbers(self):
        self.assertEqual(extract_first_letters("Word1, Word2. Word3!"), ["W", "W", "W"])
    def test_string_with_empty_words_from_multiple_spaces(self):
        self.assertEqual(extract_first_letters("One  Two   Three"), ["O", "T", "T"])
    def test_string_with_only_punctuation(self):
        self.assertEqual(extract_first_letters("!@#$%^&*()"), [])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)