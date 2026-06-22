import unittest

class GeometryUtils:

    @staticmethod
    def calculate_perimeter(length: float, width: float) -> float:
        if length < 0 or width < 0:
            raise ValueError('Length and width must be non-negative.')
        return 2 * (length + width)

class TestGeometryUtils(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(GeometryUtils.calculate_perimeter(10, 5), 30)

    def test_zero_values(self):
        self.assertEqual(GeometryUtils.calculate_perimeter(0, 0), 0)
        self.assertEqual(GeometryUtils.calculate_perimeter(10, 0), 20)
        self.assertEqual(GeometryUtils.calculate_perimeter(0, 5), 10)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(-10, 5)
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(10, -5)
        with self.assertRaises(ValueError):
            GeometryUtils.calculate_perimeter(-10, -5)
if __name__ == '__main__':
    sample_length = 7.5
    sample_width = 3.2
    perimeter = GeometryUtils.calculate_perimeter(sample_length, sample_width)
    print(f'Perimeter of rectangle with length {sample_length} and width {sample_width} is: {perimeter}')
    try:
        invalid_perimeter = GeometryUtils.calculate_perimeter(-5, 3)
    except ValueError as e:
        print(f'Caught expected error for negative input: {e}')