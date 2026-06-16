import unittest
def find_greatest_number(numbers):
    if not numbers:
        raise ValueError("Input array cannot be empty.")
    return max(numbers)
class TestFindGreatestNumber(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(find_greatest_number([42]), 42)
    def test_multiple_elements(self):
        result = find_greatest_number([-5, -10, 3, 7])
        self.assertEqual(result, 7)
    def test_all_negative_numbers(self):
        self.assertEqual(find_greatest_number([-1, -99, -2]), -1)
    def test_empty_array_raises_error(self):
        with self.assertRaises(ValueError):
            find_greatest_number([])
    def test_float_values(self):
        result = find_greatest_number([3.5, 4.0, 2.8])
        self.assertEqual(result, 4.0)
if __name__ == '__main__':
    unittest.main()