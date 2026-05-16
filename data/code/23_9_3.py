import unittest
class NumberComparator:
    def compare(self, a, b):
        if a == b:
            return 0
        elif a < b:
            return -1
        else:
            return 1
class TestNumberComparator(unittest.TestCase):
    def setUp(self):
        self.comparator = NumberComparator()
    def test_equal_numbers(self):
        self.assertEqual(self.comparator.compare(5, 5), 0)
        self.assertEqual(self.comparator.compare(0, 0), 0)
        self.assertEqual(self.comparator.compare(-10, -10), 0)
    def test_a_less_than_b(self):
        self.assertEqual(self.comparator.compare(1, 2), -1)
        self.assertEqual(self.comparator.compare(-5, 0), -1)
        self.assertEqual(self.comparator.compare(-10, -5), -1)
    def test_a_greater_than_b(self):
        self.assertEqual(self.comparator.compare(2, 1), 1)
        self.assertEqual(self.comparator.compare(10, 5), 1)
        self.assertEqual(self.comparator.compare(0, -1), 1)
    def test_positive_and_negative_mix(self):
        self.assertEqual(self.comparator.compare(10, -1), 1)
        self.assertEqual(self.comparator.compare(-10, 1), -1)
        self.assertEqual(self.comparator.compare(-5, 5), -1)
    def test_zero_involving_negatives(self):
        self.assertEqual(self.comparator.compare(0, 5), -1)
        self.assertEqual(self.comparator.compare(-5, 0), -1)
        self.assertEqual(self.comparator.compare(0, -5), 1)
        self.assertEqual(self.comparator.compare(0, 0), 0)
    def test_very_small_differences(self):
        self.assertEqual(self.comparator.compare(0.00001, 0.00002), -1)
        self.assertEqual(self.comparator.compare(-1e-6, -2e-6), -1)
        self.assertEqual(self.comparator.compare(1e-10, 1e-10 + 1e-15), -1)
        self.assertEqual(self.comparator.compare(0.0, 1e-10), -1)
        self.assertEqual(self.comparator.compare(1e-10, 0.0), 1)
    def test_large_numbers(self):
        self.assertEqual(self.comparator.compare(1000000, 1000001), -1)
        self.assertEqual(self.comparator.compare(-5000000, -5000001), -1)
        self.assertEqual(self.comparator.compare(999999999, 1000000000), -1)
        self.assertEqual(self.comparator.compare(-1000000000, -999999999), 1)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)