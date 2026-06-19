import unittest

def string_length(s):
    return len(s)

class TestStringLength(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(string_length(''), 0)

    def test_normal_string(self):
        self.assertEqual(string_length('hello'), 5)

    def test_string_with_spaces(self):
        self.assertEqual(string_length('hello world'), 11)

    def test_string_with_special_characters(self):
        self.assertEqual(string_length('!@#$%^&*()'), 10)
if __name__ == '__main__':
    print(string_length(''))
    print(string_length('hello'))
    print(string_length('hello world'))
    print(string_length('!@#$%^&*()'))
    unittest.main(argv=[''], exit=False)