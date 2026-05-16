import unittest
class TestVolumeConversion(unittest.TestCase):
    def convert_to_cubic_meters(self, volume_liters):
        return volume_liters / 1000.0
    def test_positive_conversion(self):
        self.assertAlmostEqual(self.convert_to_cubic_meters(1000), 1.0)
        self.assertAlmostEqual(self.convert_to_cubic_meters(5000), 5.0)
        self.assertAlmostEqual(self.convert_to_cubic_meters(1234.56), 1.23456)
    def test_zero_volume(self):
        self.assertEqual(self.convert_to_cubic_meters(0), 0.0)
    def test_large_numbers(self):
        self.assertAlmostEqual(self.convert_to_cubic_meters(1000000), 1000.0)
        self.assertAlmostEqual(self.convert_to_cubic_meters(999999999), 999999.999)
    def test_small_numbers(self):
        self.assertAlmostEqual(self.convert_to_cubic_meters(1), 0.001)
        self.assertAlmostEqual(self.convert_to_cubic_meters(0.5), 0.0005)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)