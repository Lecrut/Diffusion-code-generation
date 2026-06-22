import unittest

def extract_first_letters(text):
    words = text.split()
    first_letters = [word[0] for word in words if word]
    return ''.join(first_letters)

class TestExtractFirstLetters(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(extract_first_letters(''), '')
    
    def test_string_with_only_spaces(self):
        self.assertEqual(extract_first_letters('   '), '')
    
    def test_string_with_words(self):
        self.assertEqual(extract_first_letters('hello world'), 'hw')
    
    def test_string_with_mixed_punctuation(self):
        self.assertEqual(extract_first_letters('hello, world! how are you?'), 'hwhay')
    
    def test_string_with_single_word(self):
        self.assertEqual(extract_first_letters('single'), 's')
    
    def test_string_with_multiple_spaces_between_words(self):
        self.assertEqual(extract_first_letters('multiple   spaces'), 'ms')

if __name__ == '__main__':
    sample_text = "this is a sample text with multiple words"
    print(extract_first_letters(sample_text))
    unittest.main(argv=[''], exit=False)