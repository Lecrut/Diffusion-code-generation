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
        self.assertEqual(remove_spaces('  Leading and trailing spaces  '), 'Leadingandtrailingspaces')

    def test_string_with_no_spaces(self):
        self.assertEqual(remove_spaces('NoSpacesHere'), 'NoSpacesHere')

    def test_string_with_multiple_consecutive_spaces(self):
        self.assertEqual(remove_spaces('Multiple   spaces'), 'Multiplespaces')
if __name__ == '__main__':
    print(remove_spaces(''))
    print(remove_spaces('   '))
    print(remove_spaces('Hello World'))
    print(remove_spaces('  Leading and trailing spaces  '))
    print(remove_spaces('NoSpacesHere'))
    print(remove_spaces('Multiple   spaces'))
    unittest.main(argv=[''], exit=False)