import unittest

def remove_spaces(input_string):
    return input_string.replace(' ', '')

class TestRemoveSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_string_with_only_spaces(self):
        self.assertEqual(remove_spaces('   '), '')

    def test_string_with_no_spaces(self):
        self.assertEqual(remove_spaces('hello'), 'hello')

    def test_string_with_mixed_characters(self):
        self.assertEqual(remove_spaces('he ll o'), 'helloworld')

    def test_string_with_leading_and_trailing_spaces(self):
        self.assertEqual(remove_spaces('  hello world  '), 'helloworld')

    def test_string_with_multiple_consecutive_spaces(self):
        self.assertEqual(remove_spaces('hello   world'), 'helloworld')
if __name__ == '__main__':
    sample1 = '   '
    sample2 = 'hello world'
    sample3 = '  hello   world  '
    print(f"Original: '{sample1}' -> Without spaces: '{remove_spaces(sample1)}'")
    print(f"Original: '{sample2}' -> Without spaces: '{remove_spaces(sample2)}'")
    print(f"Original: '{sample3}' -> Without spaces: '{remove_spaces(sample3)}'")
    unittest.main(argv=[''], exit=False)