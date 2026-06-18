import unittest

def numbers_differ(a: float, b: float) -> bool:
    """
    Checks if two numbers differ from each other.
    
    Args:
        a (float): The first number.
        b (float): The second number.
        
    Returns:
        bool: True if the numbers are different, False otherwise.
    """
    return a != b

class TestNumbersDiffer(unittest.TestCase):
    """Test suite for the numbers_differ function."""

    def test_positive_integers(self):
        self.assertTrue(numbers_differ(10, 20))
        self.assertFalse(numbers_differ(5, 5))

    def test_negative_integers(self):
        self.assertTrue(numbers_differ(-3, -7))
        self.assertFalse(numbers_differ(-4.5, -4.5))

    def test_zero_cases(self):
        self.assertTrue(numbers_differ(0, 1))
        self.assertFalse(numbers_differ(0, 0))
        self.assertTrue(numbers_differ(-0, 1))

    def test_floating_point_numbers(self):
        self.assertTrue(numbers_differ(3.14, 2.71))
        self.assertFalse(numbers_differ(5.0, 5.0))
        # Test very close but distinct floats due to precision differences if applicable, 
        # though standard != works for exact representation equality here.
        self.assertTrue(numbers_differ(3.141592653589793, 3.14159265358979))

    def test_mixed_types_logic(self):
        # Ensure logic holds for mixed positive/negative and floats/ints combinations
        self.assertTrue(numbers_differ(0, -1))
        self.assertFalse(numbers_differ(float('inf'), float('inf')))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNumbersDiffer)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)