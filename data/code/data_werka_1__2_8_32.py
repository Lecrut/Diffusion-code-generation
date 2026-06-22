import unittest

def calculate_volume(length, width, height):
    if length < 0 or width < 0 or height < 0:
        raise ValueError('Dimensions must be non-negative')
    return length * width * height

class TestVolumeCalculation(unittest.TestCase):

    def test_positive_dimensions(self):
        self.assertEqual(calculate_volume(3, 4, 5), 60)

    def test_zero_dimension(self):
        self.assertEqual(calculate_volume(0, 4, 5), 0)
        self.assertEqual(calculate_volume(3, 0, 5), 0)
        self.assertEqual(calculate_volume(3, 4, 0), 0)

    def test_negative_dimensions(self):
        with self.assertRaises(ValueError):
            calculate_volume(-1, 4, 5)
        with self.assertRaises(ValueError):
            calculate_volume(3, -1, 5)
        with self.assertRaises(ValueError):
            calculate_volume(3, 4, -1)
if __name__ == '__main__':
    print(calculate_volume(2, 3, 4))
    unittest.main(argv=[''], exit=False)