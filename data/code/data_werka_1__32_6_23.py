import unittest

def measure_string_length(s):
    return len(s)

class TestMeasureStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(measure_string_length(''), 0)
    
    def test_normal_string(self):
        self.assertEqual(measure_string_length('hello'), 5)
    
    def test_string_with_special_characters(self):
        self.assertEqual(measure_string_length('!@#$%^&*()'), 10)
    
    def test_string_with_spaces(self):
        self.assertEqual(measure_string_length('hello world'), 11)

if __name__ == '__main__':
    sample_values = ['', 'hello', '!@#$%^&*()', 'hello world']
    for value in sample_values:
        print(f"Length of '{value}': {measure_string_length(value)}")