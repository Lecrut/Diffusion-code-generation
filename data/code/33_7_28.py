import unittest

def remove_spaces(input_string):
    return input_string.replace(" ", "")

class TestRemoveSpaces(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(remove_spaces(""), "")
    
    def test_string_with_only_spaces(self):
        self.assertEqual(remove_spaces("   "), "")
    
    def test_string_with_no_spaces(self):
        self.assertEqual(remove_spaces("hello"), "hello")
    
    def test_string_with_mixed_characters(self):
        self.assertEqual(remove_spaces("h e l l o"), "hello")
    
    def test_string_with_leading_and_trailing_spaces(self):
        self.assertEqual(remove_spaces("  hello world  "), "helloworld")
    
    def test_string_with_multiple_consecutive_spaces(self):
        self.assertEqual(remove_spaces("he   ll  o"), "helloworld")

if __name__ == '__main__':
    sample_values = [
        "",
        "   ",
        "hello",
        "h e l l o",
        "  hello world  ",
        "he   ll  o"
    ]
    
    for value in sample_values:
        print(remove_spaces(value))