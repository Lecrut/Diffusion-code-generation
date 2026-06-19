import unittest

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length.
    
    Args:
        side_length (float or int): The length of one side of the square.
        
    Returns:
        float: The calculated area.
        
    Raises:
        TypeError: If side_length is not a numeric type.
        ValueError: If side_length is negative.
    """
    if not isinstance(side_length, (int, float)):
        raise TypeError("side_length must be an integer or float")
    
    if side_length < 0:
        raise ValueError("side_length cannot be negative")
        
    return side_length * side_length

class TestSquareArea(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(calculate_square_area(5), 25)

    def test_negative_number_raises_value_error(self):
        with self.assertRaises(ValueError):
            calculate_square_area(-3)

    def test_non_numeric_type_raises_typeerror(self):
        with self.assertRaises(TypeError):
            calculate_square_area("side")

    def test_float_side_length(self):
        self.assertEqual(calculate_square_area(4.5), 20.25)

if __name__ == '__main__':
    # Sample values to demonstrate functionality without user input
    sample_tests = [1, 3, -2]
    
    print("Running manual samples...")
    for side in sample_tests:
        try:
            area = calculate_square_area(side)
            print(f"Area of square with side {side}: {area}")
        except (TypeError, ValueError) as e:
            print(f"Error for input {side}: {e}")

    # Run the unit tests to verify correctness
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSquareArea)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if not result.wasSuccessful():
        exit(1)