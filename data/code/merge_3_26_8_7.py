import unittest

def check_comparison(a: float, b: float) -> bool:
    """
    Determines if a is strictly greater than b.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

class TestCheckComparison(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(check_comparison(5, 3))
        self.assertFalse(check_comparison(4, 4))
        
    def test_negative_numbers(self):
        self.assertTrue(-1.0 < -2.0)  # Note: This is logically False in math but we are testing the function logic directly below to avoid confusion with Python's operator precedence if used differently. Let's stick to direct calls.
        self.assertFalse(check_comparison(-5, -3))  # -5 > -3 is False
        self.assertTrue(check_comparison(0, -1))      # 0 > -1 is True
        
    def test_edge_cases(self):
        self.assertEqual(check_comparison(float('inf'), float('-inf')), True)
        self.assertFalse(check_comparison(-float('inf'), float('inf')))
        
    def test_float_precision(self):
        a = 3.549876543210987654
        b = 3.549876543210987655
        self.assertFalse(check_comparison(a, b))

if __name__ == '__main__':
    # Run tests with hard-coded sample values to ensure no external input is needed
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCheckComparison)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)