import unittest

def check_comparison(a: int, b: int) -> bool:
    """Returns True if a is strictly greater than b, False otherwise."""
    return a > b

class TestCheckComparison(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertTrue(check_comparison(5, 3))
        self.assertFalse(check_comparison(4, 5))

    def test_zero_handling(self):
        self.assertTrue(check_comparison(0, -1))
        self.assertFalse(check_comparison(-1, 0))

    def test_negative_numbers(self):
        self.assertTrue(check_comparison(-2, -5))
        self.assertFalse(check_comparison(-3, -2))

    def test_edge_case_equal_values(self):
        # When a equals b, the condition "a > b" is False.
        result = check_comparison(10, 10)
        self.assertEqual(result, False)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCheckComparison)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)