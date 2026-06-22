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
        self.assertEqual(GeometryUtils.calculate_perimeter(5, 0), 10)
        self.assertEqual(GeometryUtils.calculate_perimeter(0, 7), 14)
    
    def test_negative_values(self):
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(-3, 4)
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(3, -4)
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(-3, -4)

if __name__ == '__main__':
    sample_length = 8.0
    sample_width = 6.0
    try:
        perimeter = GeometryUtils.calculate_perimeter(sample_length, sample_width)
        print(perimeter)
    except ValueError as e:
        print(e)