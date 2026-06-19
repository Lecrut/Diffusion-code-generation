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
    sample1 = '  Hello World  '
    sample2 = 'NoSpacesHere'
    sample3 = '   '
    print(remove_spaces(sample1))
    print(remove_spaces(sample2))
    print(remove_spaces(sample3))
    unittest.main(argv=[''], exit=False)