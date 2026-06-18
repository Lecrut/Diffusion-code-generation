import unittest
def find_greatest_number(numbers):
    if not numbers:
        raise ValueError("Input array must contain at least one element.")
    return max(numbers)
class TestFindGreatestNumber(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(find_greatest_number([42]), 42)
    def test_multiple_elements(self):
        data = [-10, -5, 0, 3, 7]
        expected = 7
        result = find_greatest_number(data)
        self.assertEqual(result, expected)
    def test_negative_numbers_only(self):
        data = [-99, -88, -12]
        expected = -12
        result = find_greatest_number(data)
        self.assertEqual(result, expected)
    def test_empty_array_raises_error(self):
        with self.assertRaises(ValueError):
            find_greatest_number([])
    def test_duplicate_max_values(self):
        data = [5, 3, 8, 8, 2]
        expected = 8
        result = find_greatest_number(data)
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()