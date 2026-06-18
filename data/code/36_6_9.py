import unittest

def reverse_string(text: str) -> str:
    """Reverse a given string without modifying it in place.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: A new string with the characters of the input in reverse order.
    """
    return text[::-1]

class TestStringReversal(unittest.TestCase):
    def test_empty_string(self):
        result = reverse_string("")
        self.assertEqual(result, "")

    def test_single_character(self):
        result = reverse_string("a")
        self.assertEqual(result, "a")

    def test_normal_case(self):
        input_text = "Hello World"
        expected_output = "dlroW olleH"
        result = reverse_string(input_text)
        self.assertEqual(result, expected_output)

    def test_special_characters_and_spaces(self):
        input_text = "!@#$%^&*()"
        expected_output = "()*&^%$#@!"
        result = reverse_string(input_text)
        self.assertEqual(result, expected_output)

    def test_unicode_support(self):
        input_text = "你好世界"
        expected_output = "界世好你"
        result = reverse_string(input_text)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    pass
