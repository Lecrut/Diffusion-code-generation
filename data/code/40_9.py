import unittest
def extract_first_letter(text):
    words = text.split()
    first_letters = []
    for word in words:
        if word:
            first_letters.append(word[0])
    return list(first_letters)
class TestExtractFirstLetter(unittest.TestCase):
    def test_normal_sentence(self):
        self.assertEqual(extract_first_letter("Hello world"), ['H', 'w'])
    def test_empty_string(self):
        self.assertEqual(extract_first_letter(""), [])
    def test_string_with_only_spaces(self):
        self.assertEqual(extract_first_letter("   \t "), [])
    def test_single_word(self):
        self.assertEqual(extract_first_letter("Single"), ['S'])
    def test_multiple_spaces(self):
        self.assertEqual(extract_first_letter("One   two"), ['O', 't'])
    def test_string_with_punctuation(self):
        self.assertEqual(extract_first_letter("Hello, world!"), ['H', 'w'])
    def test_punctuation_attached_to_words(self):
        self.assertEqual(extract_first_letter("Word1, Word2."), ['W', 'W'])
    def test_empty_words_from_splitting(self):
        self.assertEqual(extract_first_letter("word1,,word2"), ['w', 'w'])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)