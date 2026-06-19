import unittest

def extract_first_letters(text):
    if not text.strip():
        return ''
    words = text.split()
    return ''.join(word[0] for word in words)

class TestExtractFirstLetters(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(extract_first_letters(''), '')

    def test_string_with_only_spaces(self):
        self.assertEqual(extract_first_letters('   '), '')

    def test_single_word(self):
        self.assertEqual(extract_first_letters('hello'), 'h')

    def test_multiple_words(self):
        self.assertEqual(extract_first_letters('hello world'), 'hw')

    def test_mixed_punctuation(self):
        self.assertEqual(extract_first_letters('hello, world! how are you?'), 'hwahy')

    def test_single_letter_words(self):
        self.assertEqual(extract_first_letters('a b c d'), 'abcd')

    def test_capitalization(self):
        self.assertEqual(extract_first_letters('Hello World'), 'HW')

if __name__ == '__main__':
    print(extract_first_letters('This is a test string.'))
    unittest.main(argv=[''], exit=False)