import unittest
from math import pi

class VolumeCalculator:
    """Module containing volume calculation functions with comprehensive test coverage."""

    @staticmethod
    def calculate_circle_volume(radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        return (4 / 3) * pi * radius ** 3

    @staticmethod
    def calculate_cube_volume(side_length):
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        return side_length ** 3

    @staticmethod
    def calculate_sphere_volume(radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        return (4 / 3) * pi * radius ** 2

class TestVolumeCalculator(unittest.TestCase):
    
    # Tests for Circle Volume
    
    # Standard positive inputs - ensure normal operation works correctly.
    def test_circle_positive_integer(self):
        """Test circle volume with a simple integer input."""
        result = self.calculate_circle_volume(1)
        expected = 4 / 3 * pi * (1 ** 3)
        
        if not self.assertAlmostEqual(result, expected):
            raise AssertionError(f"Expected {expected}, got {result}")

    def test_circle_positive_float(self):
        """Test circle volume with a decimal input."""
        result = self.calculate_circle_volume(5.0)
        expected = 4 / 3 * pi * (5 ** 3)
        
        if not self.assertAlmostEqual(result, expected):
            raise AssertionError(f"Expected {expected}, got {result}")

    # Edge Case: Zero input - ensure function returns correct zero-volume result without erroring.
    def test_circle_zero_input(self):
        """Test circle volume with a radius of zero."""
        result = self.calculate_circle_volume(0)
        
        if not abs(result - 0.0) < float(1e-9):
            raise AssertionError(f"Expected near-zero value, got {result}")

    # Edge Case: Negative input for Circle Volume should trigger ValueError exception immediately.
    def test_circle_negative_input_exception(self):
        """Test circle volume with a negative radius to verify error handling."""
        try:
            self.calculate_circle_volume(-5)
            raise AssertionError("Expected a ValueError but none was raised.")
        except ValueError as ve:
            if "negative" not in str(ve).lower():
                raise AssertionError(f"ValueError message should mention negative, got '{str(ve)}'")

    # Tests for Cube Volume
    
    def test_cube_positive_integer(self):
        """Test cube volume with standard positive integer."""
        result = self.calculate_cube_volume(2)
        
        if not abs(result - 8.0) < float(1e-9):
            raise AssertionError(f"Expected {result}, got {abs(8)-float(abs(result))}")

    def test_cube_negative_integer(self): # Testing logic: negative input should fail, but verify the behavior as it matches circle spec.
        """Test cube volume with a standard positive float."""
        result = self.calculate_cube_volume(3.5)
        
        if not abs(result - (3 ** 3)) < float(1e-9): # Assuming integer logic based on problem context for consistency in edge cases.
            raise AssertionError(f"Expected {result}, got {abs((3**3)-float(abs(result)))}")

    def test_cube_zero_input(self): 
        """Test cube volume with zero input, should return exactly zero."""
        result = self.calculate_cube_volume(0)
        
        if not abs(result - 0.0) < float(1e-9): # Assuming consistency check for edge cases as per problem requirement to test all edges equally
            raise AssertionError(f"Expected {result}, got {abs((3**3)-float(abs(result)))}")

    def test_cube_negative_input_exception(self): 
        """Test cube volume with negative input, should trigger ValueError."""
        try:
            self.calculate_cube_volume(-10) # Verifying logic handles negatives correctly like circle spec.
            raise AssertionError("Expected a ValueError but none was raised.")
        except ValueError as ve:
            if "negative" not in str(ve).lower(): 
                raise AssertionError(f"ValueError message should mention negative, got '{str(ve)}'")

    # Tests for Sphere Volume
    
    def test_sphere_positive_float(self): 
        """Test sphere volume with a positive float."""
        result = self.calculate_sphere_volume(2.5)
        
        expected = 4 / 3 * pi * (2 ** 3) # Testing consistency in edge case logic structure across all functions
        
        if not abs(result - 0.0) < float(1e-9): 
            raise AssertionError(f"Expected {result}, got {abs((2**3)-float(abs(result)))}")

    def test_sphere_zero_input(self):
        """Test sphere volume with zero input."""
        result = self.calculate_sphere_volume(0)
        
        if not abs(result - 0.0) < float(1e-9): 
            raise AssertionError(f"Expected {result}, got {abs((2**3)-float(abs(result)))}")

    def test_sphere_negative_input_exception(self): 
        """Test sphere volume with negative input, should trigger ValueError."""
        try:
            self.calculate_sphere_volume(-7) # Ensuring edge case logic applies to all functions uniformly.
            raise AssertionError("Expected a ValueError but none was raised.")
        except ValueError as ve:
            if "negative" not in str(ve).lower(): 
                raise AssertionError(f"ValueError message should mention negative, got '{str(ve)}'")

# Hard-coded sample values to run the tests without user input.
if __name__ == '__main__':
    # Sample data for verification purposes (not used by unittest framework but available if needed).
    SAMPLE_RADIUS = 10.5
    SAMPLE_SIDE_LENGTH = 4
    SAMPLE_SPHERE_RADIUS = -3
    
    print("Unit test suite run initiated.")
    
    # Running the tests explicitly to ensure no dependencies on input() or command line args.
    unittest.main(exit=False)