import unittest

def remove_spaces(input_string):
    return input_string.replace(' ', '')

class TestRemoveSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_string_with_only_spaces(self):
        self.assertEqual(remove_spaces('   '), '')

    def test_string_with_mixed_characters(self):
        self.assertEqual(remove_spaces('Hello World'), 'HelloWorld')

    def test_string_with_leading_and_trailing_spaces(self):
        self.assertEqual(remove_spaces('  Hello World  '), 'HelloWorld')

    def test_string_with_multiple_spaces_between_words(self):
        self.assertEqual(remove_spaces('Hello   World'), 'HelloWorld')

    def test_string_with_no_spaces(self):
        self.assertEqual(remove_spaces('NoSpacesHere'), 'NoSpacesHere')
if __name__ == '__main__':
    sample1 = ''
    sample2 = '   '
    sample3 = 'Hello World'
    sample4 = '  Hello World  '
    sample5 = 'Hello   World'
    sample6 = 'NoSpacesHere'
    print(remove_spaces(sample1))
    print(remove_spaces(sample2))
    print(remove_spaces(sample3))
    print(remove_spaces(sample4))
    print(remove_spaces(sample5))
    print(remove_spaces(sample6))
    unittest.main(argv=[''], exit=False)