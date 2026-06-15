import unittest
def calculate_median(data):
    if not data:
        raise ValueError("Input list cannot be empty")
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
        data = [1, 3, 2]
        self.assertEqual(calculate_median(data), 2)
    def test_even_length_list(self):
        data = [1, 5, 2, 4]
        self.assertAlmostEqual(calculate_median(data), 3.0)
    def test_list_with_duplicates(self):
        data = [5, 2, 8, 5, 1]
        self.assertEqual(calculate_median(data), 5)
    def test_empty_list(self):
        with self.assertRaisesRegex(ValueError, "Input list cannot be empty"):
            calculate_median([])
    def test_single_element_list(self):
        data = [42]
        self.assertEqual(calculate_median(data), 42)
    def test_negative_numbers(self):
        data = [-10, -5, 0]
        self.assertEqual(calculate_median(data), -5)
    def test_large_even_list(self):
        data = [100, 200, 300, 400]
        self.assertAlmostEqual(calculate_median(data), 250.0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)