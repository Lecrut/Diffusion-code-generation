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
    
    def test_string_with_unicode_characters(self):
        self.assertEqual(string_length('你好世界'), 4)

if __name__ == '__main__':
    print("Testing string_length function:")
    print(f"Length of '': {string_length('')}")
    print(f"Length of 'hello': {string_length('hello')}")
    print(f"Length of '!@#$%^&*()': {string_length('!@#$%^&*()')}")
    print(f"Length of '你好世界': {string_length('你好世界')}")
    
    unittest.main(argv=[''], exit=False)