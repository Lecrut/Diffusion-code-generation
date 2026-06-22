import unittest

class GeometryUtils:
    @staticmethod
    def validate_dimensions(length: float, width: float) -> bool:
        if length <= 0 or width <= 0:
            return False
        return True

    @staticmethod
    def calculate_perimeter(length: float, width: float) -> float:
        if not GeometryUtils.validate_dimensions(length, width):
            raise ValueError("Length and width must be positive numbers")
        return 2 * (length + width)

class TestGeometryUtils(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(GeometryUtils.calculate_perimeter(10.0, 5.0), 30.0)
    
    def test_zero_length(self):
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(0, 5.0)
    
    def test_negative_length(self):
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(-10.0, 5.0)
    
    def test_zero_width(self):
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(10.0, 0)
    
    def test_negative_width(self):
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(10.0, -5.0)
    
    def test_large_values(self):
        self.assertEqual(GeometryUtils.calculate_perimeter(1000000.0, 500000.0), 3000000.0)
    
    def test_small_values(self):
        self.assertAlmostEqual(GeometryUtils.calculate_perimeter(0.001, 0.002), 0.006, places=3)

if __name__ == '__main__':
    sample_length = 7.5
    sample_width = 3.2
    try:
        perimeter = GeometryUtils.calculate_perimeter(sample_length, sample_width)
        print(perimeter)
    except ValueError as e:
        print(e)