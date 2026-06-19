import unittest

class GeometryUtils:
    @staticmethod
    def calculate_perimeter(length: float, width: float) -> float:
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative")
        return 2 * (length + width)

class TestGeometryUtils(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(GeometryUtils.calculate_perimeter(3, 4), 14)
    
    def test_zero_values(self):
        self.assertEqual(GeometryUtils.calculate_perimeter(0, 0), 0)
    
    def test_single_zero_value(self):
        self.assertEqual(GeometryUtils.calculate_perimeter(0, 5), 10)
        self.assertEqual(GeometryUtils.calculate_perimeter(5, 0), 10)
    
    def test_negative_values(self):
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(-3, 4)
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(3, -4)
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(-3, -4)

if __name__ == '__main__':
    sample_length = 7.5
    sample_width = 2.5
    try:
        perimeter = GeometryUtils.calculate_perimeter(sample_length, sample_width)
        print(f"Perimeter: {perimeter}")
    except ValueError as e:
        print(e)