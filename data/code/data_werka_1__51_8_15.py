import unittest

class GeometryUtils:
    DEFAULT_LENGTH = 10.0
    DEFAULT_WIDTH = 5.0
    
    @staticmethod
    def calculate_perimeter(length: float, width: float) -> float:
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative")
        return 2 * (length + width)
    
    @staticmethod
    def _validate_input(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number")

class TestGeometryUtils(unittest.TestCase):
    
    def test_positive_values(self):
        self.assertEqual(GeometryUtils.calculate_perimeter(10, 5), 30)
    
    def test_zero_values(self):
        self.assertEqual(GeometryUtils.calculate_perimeter(0, 0), 0)
    
    def test_negative_length(self):
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(-1, 5)
    
    def test_negative_width(self):
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(10, -1)
    
    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            GeometryUtils.calculate_perimeter('a', 5)
    
    def test_default_values(self):
        self.assertEqual(GeometryUtils.calculate_perimeter(GeometryUtils.DEFAULT_LENGTH, GeometryUtils.DEFAULT_WIDTH), 30)

if __name__ == '__main__':
    sample_length = 7.5
    sample_width = 3.2
    try:
        perimeter = GeometryUtils.calculate_perimeter(sample_length, sample_width)
        print(perimeter)
    except Exception as e:
        print(f"Error: {e}")