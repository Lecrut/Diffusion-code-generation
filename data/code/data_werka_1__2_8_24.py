import unittest

def calculate_volume(length, width, height):
    if length < 0 or width < 0 or height < 0:
        raise ValueError('Dimensions must be non-negative')
    return length * width * height

class TestVolumeCalculation(unittest.TestCase):

    def test_positive_dimensions(self):
        self.assertEqual(calculate_volume(2, 3, 4), 24)

    def test_zero_dimension(self):
        self.assertEqual(calculate_volume(0, 3, 4), 0)
        self.assertEqual(calculate_volume(2, 0, 4), 0)
        self.assertEqual(calculate_volume(2, 3, 0), 0)

    def test_negative_dimensions(self):
        with self.assertRaises(ValueError):
            calculate_volume(-1, 3, 4)
        with self.assertRaises(ValueError):
            calculate_volume(2, -3, 4)
        with self.assertRaises(ValueError):
            calculate_volume(2, 3, -4)

    def test_large_dimensions(self):
        self.assertEqual(calculate_volume(1000, 1000, 1000), 1000000000)
if __name__ == '__main__':
    print('Volume of a 2x3x4 box:', calculate_volume(2, 3, 4))
    print('Volume of a 0x3x4 box:', calculate_volume(0, 3, 4))
    print('Volume of a 2x0x4 box:', calculate_volume(2, 0, 4))
    print('Volume of a 2x3x0 box:', calculate_volume(2, 3, 0))