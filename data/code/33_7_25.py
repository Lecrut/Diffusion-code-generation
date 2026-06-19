import unittest

def remove_spaces(input_string):
    return input_string.replace(" ", "")

class TestRemoveSpaces(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(remove_spaces(""), "")
    
    def test_only_spaces(self):
        self.assertEqual(remove_spaces("   "), "")
    
    def test_no_spaces(self):
        self.assertEqual(remove_spaces("abc"), "abc")
    
    def test_mixed_characters(self):
        self.assertEqual(remove_spaces("a b c d e"), "abcde")
    
    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_spaces("  hello world  "), "helloworld")
    
    def test_multiple_consecutive_spaces(self):
        self.assertEqual(remove_spaces("a   b"), "ab")

if __name__ == '__main__':
    sample_values = [
        "",
        "   ",
        "abc",
        "a b c d e",
        "  hello world  ",
        "a   b"
    ]
    
    for value in sample_values:
        print(remove_spaces(value))