import unittest
class TestVolumeConversion(unittest.TestCase):
    def convert_to_liters(self, volume_ml):
        return volume_ml / 1000.0
    def test_positive_conversion(self):
        self.assertAlmostEqual(self.convert_to_liters(1000), 1.0)
        self.assertAlmostEqual(self.convert_to_liters(500), 0.5)
        self.assertAlmostEqual(self.convert_to_liters(2500), 2.5)
        self.assertAlmostEqual(self.convert_to_liters(1234.56), 1.23456)
    def test_zero_volume(self):
        self.assertEqual(self.convert_to_liters(0), 0.0)
    def test_large_numbers(self):
        self.assertAlmostEqual(self.convert_to_liters(1000000), 1000.0)
        self.assertAlmostEqual(self.convert_to_liters(999999.99), 999.999999)
    def test_small_numbers(self):
        self.assertAlmostEqual(self.convert_to_liters(1), 0.001)
        self.assertAlmostEqual(self.convert_to_liters(0.5), 0.0005)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)