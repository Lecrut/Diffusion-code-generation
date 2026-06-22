import unittest

def measure_string_length(s):
    return len(s)

class TestStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(measure_string_length(''), 0)
    
    def test_normal_string(self):
        self.assertEqual(measure_string_length('hello'), 5)
    
    def test_string_with_special_characters(self):
        self.assertEqual(measure_string_length('hello!@#'), 8)
    
    def test_whitespace_only_string(self):
        self.assertEqual(measure_string_length('   '), 3)

if __name__ == '__main__':
    sample_values = [
        '',
        'hello',
        'hello!@#',
        '   '
    ]
    for value in sample_values:
        print(f"Length of '{value}': {measure_string_length(value)}")