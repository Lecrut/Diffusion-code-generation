import unittest

def measure_string_length(s):
    return len(s)

class TestMeasureStringLength(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(measure_string_length(''), 0)

    def test_normal_string(self):
        self.assertEqual(measure_string_length('hello'), 5)

    def test_string_with_spaces(self):
        self.assertEqual(measure_string_length('hello world'), 11)

    def test_string_with_special_characters(self):
        self.assertEqual(measure_string_length('!@#$%^&*()'), 10)

    def test_string_with_mixed_content(self):
        self.assertEqual(measure_string_length('Hello, World!'), 13)
if __name__ == '__main__':
    print("String length of '':", measure_string_length(''))
    print("String length of 'hello world':", measure_string_length('hello world'))
    print("String length of '!@#$%^&*()':", measure_string_length('!@#$%^&*()'))
    unittest.main(argv=[''], exit=False)