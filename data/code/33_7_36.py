import unittest

def remove_spaces(input_string):
    return input_string.replace(' ', '')

class TestRemoveSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_only_spaces(self):
        self.assertEqual(remove_spaces('   '), '')

    def test_no_spaces(self):
        self.assertEqual(remove_spaces('abc'), 'abc')

    def test_mixed_characters(self):
        self.assertEqual(remove_spaces('a b c d'), 'abcd')

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_spaces('  hello world  '), 'helloworld')

    def test_multiple_consecutive_spaces(self):
        self.assertEqual(remove_spaces('a   b'), 'ab')
if __name__ == '__main__':
    sample1 = remove_spaces('')
    sample2 = remove_spaces('   ')
    sample3 = remove_spaces('abc')
    sample4 = remove_spaces('a b c d')
    sample5 = remove_spaces('  hello world  ')
    sample6 = remove_spaces('a   b')
    print(sample1)
    print(sample2)
    print(sample3)
    print(sample4)
    print(sample5)
    print(sample6)
    unittest.main(argv=[''], exit=False)