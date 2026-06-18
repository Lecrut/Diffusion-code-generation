import unittest

def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.
    
    Args:
        side_length (float or int): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If the side length is negative.
        TypeError: If the side length is not a number.
    """
    if isinstance(side_length, (int, float)):
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        return side_length ** 2
    else:
        raise TypeError("Side length must be an integer or float.")

class TestSquareArea(unittest.TestCase):
    
    def test_positive_integer(self):
        self.assertEqual(calculate_square_area(5), 25)

    def test_positive_float(self):
        self.assertAlmostEqual(calculate_square_area(3.14), 9.8596, places=4)

    def test_zero_side_length(self):
        self.assertEqual(calculate_square_area(0), 0)

    def test_negative_side_length_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_square_area(-2)

    def test_non_numeric_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            calculate_square_area("5")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSquareArea)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Run a manual example to demonstrate functionality without input prompts
    print("\n--- Manual Test Execution ---")
    
    sample_side = 7.0
    area_result = calculate_square_area(sample_side)
    expected_area = 49.0
    
    assert abs(area_result - expected_area) < float('eps'), "Manual test failed."

    # Print the result of manual execution to confirm it works as intended without user input
    print(f"Sample side length: {sample_side}")
    print(f"Calculated area: {area_result}")