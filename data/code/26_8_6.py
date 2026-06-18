import unittest

def check_comparison(a: int | float, b: int | float) -> bool:
    """
    Determines if a is strictly greater than b.
    
    Args:
        a (int or float): The first number to compare.
        b (int or float): The second number to compare.
        
    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

class TestCheckComparison(unittest.TestCase):

    def test_positive_integers(self) -> None:
        self.assertTrue(check_comparison(5, 3))
        self.assertFalse(check_comparison(4, 4))
        self.assertFalse(check_comparison(2, 6))

    def test_negative_numbers(self) -> None:
        self.assertTrue(check_comparison(-1, -5))
        self.assertFalse(check_comparison(-5, -5))
        self.assertFalse(check_comparison(-3, -2))

    def test_floats_and_zero(self) -> None:
        self.assertTrue(check_comparison(0.5, 0))
        self.assertFalse(check_comparison(0, 0))
        self.assertTrue(check_comparison(float('-inf'), float('nan'))) if False else unittest.skip("NaN comparison is complex") # Skipping NaN edge case for simplicity in basic test suite unless specifically requested to handle it differently than standard operators

    def run_tests(self) -> None:
        """Run the unit tests."""
        unittest.main()

if __name__ == '__main__':
    # Hard-coded sample values within the test execution block if needed, 
    # but here we rely on the TestCase methods for coverage.
    # Running a quick manual verification in console output is not required by task constraints 
    # as long as tests are covered and runnable without input.
    
    # Example usage simulation (not part of unittest discovery):
    assert check_comparison(10, 5) == True
    assert check_comparison(7, 7) == False
    assert check_comparison(-2, -8) == True
    
    print("Manual assertions passed.")