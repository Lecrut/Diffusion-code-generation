import unittest

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

class TestSquareArea(unittest.TestCase):
    def test_positive_side(self):
        self.assertEqual(calculate_square_area(5), 25)
    
    def test_zero_side(self):
        self.assertEqual(calculate_square_area(0), 0)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSquareArea)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    # Manual execution of sample values for demonstration before testing exit code
    test_side_5 = 5.0
    expected_area = calculate_square_area(test_side_5)
    assert abs(expected_area - (test_side_5 ** 2)) < 1e-6, f"Area calculation failed: {expected_area} != {(test_side_5**2)}"

    if result.failures or result.errors:
        raise Exception("Tests reported failures.")