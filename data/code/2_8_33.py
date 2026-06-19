import unittest

def calculate_volume(length, width, height):
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive numbers")
    return length * width * height

class TestVolumeCalculation(unittest.TestCase):

    def test_positive_dimensions(self):
        self.assertEqual(calculate_volume(2, 3, 4), 24)

    def test_zero_dimension(self):
        with self.assertRaises(ValueError):
            calculate_volume(0, 3, 4)

    def test_negative_dimension(self):
        with self.assertRaises(ValueError):
            calculate_volume(-1, 3, 4)

    def test_all_zero_dimensions(self):
        with self.assertRaises(ValueError):
            calculate_volume(0, 0, 0)

    def test_all_negative_dimensions(self):
        with self.assertRaises(ValueError):
            calculate_volume(-1, -2, -3)

    def test_mixed_sign_dimensions(self):
        with self.assertRaises(ValueError):
            calculate_volume(-1, 2, 3)

if __name__ == '__main__':
    try:
        print(calculate_volume(5, 6, 7))
    except Exception as e:
        print(e)