import unittest
def find_greatest_number(numbers):
    if not numbers:
        raise ValueError("Input array cannot be empty.")
    try:
        return max(numbers)
    except TypeError:
        raise ValueError("All elements must be comparable numeric types.")
class TestFindGreatestNumber(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(find_greatest_number([42]), 42)
    def test_multiple_elements(self):
        result = find_greatest_number([-10, -5, 0, 3, 7])
        self.assertEqual(result, 7)
    def test_negative_only(self):
        self.assertEqual(find_greatest_number([-99, -88, -1]), -1)
    def test_float_values(self):
        result = find_greatest_number([1.5, 2.3, 0.1])
        self.assertAlmostEqual(result, 2.3)
    def test_empty_array_raises_error(self):
        with self.assertRaises(ValueError):
            find_greatest_number([])
if __name__ == '__main__':
    unittest.main()