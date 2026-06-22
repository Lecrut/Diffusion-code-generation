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

    def test_palindrome(self):
        self.assertEqual(reverse_string('racecar'), 'racecar')

if __name__ == '__main__':
    sample_values = ['', 'a', 'hello', 'hello world', 'racecar']
    for value in sample_values:
        print(f"Original: {value}, Reversed: {reverse_string(value)}")