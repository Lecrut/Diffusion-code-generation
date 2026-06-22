import unittest

class GeometryUtils:
    @staticmethod
    def calculate_perimeter(length: float, width: float) -> float:
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        return 2 * (length + width)

class TestGeometryUtils(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(GeometryUtils.calculate_perimeter(3, 4), 14)
        self.assertEqual(GeometryUtils.calculate_perimeter(5.5, 2.5), 16)

    def test_zero_value(self):
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(0, 5)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(-3, 4)

    def test_both_zero(self):
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(0, 0)

    def test_both_negative(self):
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(-1, -2)

if __name__ == '__main__':
    sample_length = 7.0
    sample_width = 3.0
    try:
        perimeter = GeometryUtils.calculate_perimeter(sample_length, sample_width)
        print(perimeter)
    except ValueError as e:
        print(e)