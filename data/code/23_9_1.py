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
        self.assertEqual(self.comparator.compare(-10.5, -10.5), 0)
    def test_a_less_than_b(self):
        self.assertEqual(self.comparator.compare(1, 2), -1)
        self.assertEqual(self.comparator.compare(-5, 0), -1)
        self.assertEqual(self.comparator.compare(-10, -5), -1)
        self.assertEqual(self.comparator.compare(0, 100), -1)
    def test_a_greater_than_b(self):
        self.assertEqual(self.comparator.compare(10, 5), 1)
        self.assertEqual(self.comparator.compare(5, -1), 1)
        self.assertEqual(self.comparator.compare(-10, -20), 1)
        self.assertEqual(self.comparator.compare(0, -1), 1)
    def test_zero_involving_negatives(self):
        self.assertEqual(self.comparator.compare(0, -5), 1)
        self.assertEqual(self.comparator.compare(-5, 0), -1)
        self.assertEqual(self.comparator.compare(0, 0), 0)
    def test_small_differences(self):
        self.assertEqual(self.comparator.compare(0.00001, 0.00002), -1)
        self.assertEqual(self.comparator.compare(1.0, 1.000000001), -1)
        self.assertEqual(self.comparator.compare(-0.000001, 0), -1)
        self.assertEqual(self.comparator.compare(0, 1e-10), -1)
        self.assertEqual(self.comparator.compare(1e-10, 0), 1)
    def test_large_numbers(self):
        self.assertEqual(self.comparator.compare(1000000, 1000001), -1)
        self.assertEqual(self.comparator.compare(-999999, -1000000), -1)
        self.assertEqual(self.comparator.compare(1000001, 1000000), 1)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)