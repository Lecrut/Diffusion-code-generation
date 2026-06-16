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
    def test_negative_numbers_only(self):
        self.assertEqual(find_greatest_number([-99, -88]), -88)
    def test_zero_and_positives(self):
        result = find_greatest_number([0, 1, 2])
        self.assertEqual(result, 2)
    def test_empty_array_raises_error(self):
        with self.assertRaises(ValueError):
            find_greatest_number([])
if __name__ == '__main__':
    unittest.main()