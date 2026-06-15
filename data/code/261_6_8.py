import unittest
def calculate_median(data):
    if not data:
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2
class TestMedianCalculation(unittest.TestCase):
    def test_odd_length_list(self):
        self.assertEqual(calculate_median([1, 3, 2]), 2)
        self.assertEqual(calculate_median([5, 1, 4, 2, 3]), 3)
    def test_even_length_list(self):
        self.assertAlmostEqual(calculate_median([1, 2, 3, 4]), 2.5)
        self.assertAlmostEqual(calculate_median([10, 20, 30, 40]), 25.0)
    def test_list_with_duplicates(self):
        self.assertEqual(calculate_median([1, 2, 2, 3, 3]), 2)
        self.assertAlmostEqual(calculate_median([1, 1, 2, 2, 3, 3]), 2.5)
    def test_empty_list(self):
        self.assertIsNone(calculate_median([]))
    def test_single_element_list(self):
        self.assertEqual(calculate_median([42]), 42)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)