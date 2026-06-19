import unittest

def reverse_string(s):
    return s[::-1]

class TestReverseString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse_string(''), '')

    def test_single_character(self):
        self.assertEqual(reverse_string('a'), 'a')

    def test_multiple_characters(self):
        self.assertEqual(reverse_string('hello'), 'olleh')

    def test_with_spaces(self):
        self.assertEqual(reverse_string('hello world'), 'dlrow olleh')

    def test_with_punctuation(self):
        self.assertEqual(reverse_string('!hello, world!'), '!dlrow ,olleh!')

if __name__ == '__main__':
    sample_input = "Alibaba Cloud"
    print(reverse_string(sample_input))