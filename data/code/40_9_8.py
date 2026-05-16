import unittest
def extract_first_letters(text):
    words = text.split()
    first_letters = []
    for word in words:
        if word:
            first_letters.append(word[0])
    return first_letters
class TestExtractFirstLetters(unittest.TestCase):
    def test_normal_string(self):
        self.assertEqual(extract_first_letters("Hello world"), ['H', 'w'])
    def test_empty_string(self):
        self.assertEqual(extract_first_letters(""), [])
    def test_string_with_only_spaces(self):
        self.assertEqual(extract_first_letters("   \t "), [])
    def test_string_with_leading_and_trailing_spaces(self):
        self.assertEqual(extract_first_letters("  Test case "), ['T', 'c'])
    def test_string_with_mixed_punctuation(self):
        self.assertEqual(extract_first_letters("Hello, world!"), ['H', 'w'])
    def test_string_with_multiple_spaces(self):
        self.assertEqual(extract_first_letters("One   two   three"), ['O', 't', 't'])
    def test_string_with_empty_words_from_punctuation(self):
        self.assertEqual(extract_first_letters("Word1, Word2."), ['W', 'W'])
    def test_string_with_only_punctuation(self):
        self.assertEqual(extract_first_letters("!@#$%^&*()"), [])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)