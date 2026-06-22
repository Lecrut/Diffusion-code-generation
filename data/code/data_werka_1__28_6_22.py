import unittest

def is_larger_than_zero(value):
    return value > 0

class TestIsLargerThanZero(unittest.TestCase):
    
    def test_positive_number(self):
        self.assertTrue(is_larger_than_zero(10))
    
    def test_negative_number(self):
        self.assertFalse(is_larger_than_zero(-5))
    
    def test_zero(self):
        self.assertFalse(is_larger_than_zero(0))
    
    def test_large_positive_number(self):
        self.assertTrue(is_larger_than_zero(999999))
    
    def test_small_negative_number(self):
        self.assertFalse(is_larger_than_zero(-1))

if __name__ == '__main__':
    sample_values = [10, -5, 0, 999999, -1]
    for value in sample_values:
        result = is_larger_than_zero(value)
        print(f"is_larger_than_zero({value}) = {result}")
    
    unittest.main(argv=[''], exit=False)