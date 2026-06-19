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

    def test_string_with_leading_trailing_spaces(self):
        self.assertEqual(remove_spaces('  Hello World  '), 'HelloWorld')

    def test_string_with_multiple_spaces_between_words(self):
        self.assertEqual(remove_spaces('Hello   World'), 'HelloWorld')

    def test_string_with_no_spaces(self):
        self.assertEqual(remove_spaces('NoSpacesHere'), 'NoSpacesHere')
if __name__ == '__main__':
    sample_input_1 = '  Hello World  '
    sample_input_2 = 'NoSpacesHere'
    sample_input_3 = '   '
    print('Sample Input:', sample_input_1)
    print('Output:', remove_spaces(sample_input_1))
    print('Sample Input:', sample_input_2)
    print('Output:', remove_spaces(sample_input_2))
    print('Sample Input:', sample_input_3)
    print('Output:', remove_spaces(sample_input_3))
    unittest.main(argv=[''], exit=False)