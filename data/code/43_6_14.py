square_area.py
"""
Module containing a function to calculate the area of a square and its unit tests.
This module is self-contained and does not require any external dependencies, files, or user input.
"""

def calculate_square_area(side_length: float) -> float:
    """
    Calculate the area of a square given its side length.

    Args:
        side_length (float): The length of one side of the square. Must be non-negative.

    Returns:
        float: The calculated area of the square.

    Raises:
        ValueError: If the side_length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side_length ** 2

class TestSquareArea(unittest.TestCase):
    """Unit tests for the calculate_square_area function."""

    def test_positive_integer(self):
        self.assertEqual(calculate_square_area(5), 25)

    def test_zero_side_length(self):
        self.assertAlmostEqual(calculate_square_area(0.0), 0.0)

    def test_negative_input_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_square_area(-3.0)

    def test_decimal_side_length(self):
        expected = 4.25 * 4.25
        self.assertAlmostEqual(calculate_square_area(4.25), expected, places=10)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or file I/O
    
    print("Sample Calculation:")
    
    side_a = 7.0
    area_a = calculate_square_area(side_a)
    print(f"Side length: {side_a}")
    print(f"Calculated Area: {area_a}")

    # Verify correctness directly here as well to ensure the function works before tests run
    assert abs(area_a - side_a ** 2) < 1e-9, "Sample calculation verification failed."
    
    print("\nRunning Unit Tests...")
    unittest.main(verbosity=2)