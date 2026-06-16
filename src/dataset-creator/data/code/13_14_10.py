import unittest
def find_greatest_number(numbers):
    if not numbers:
        raise ValueError("Input array cannot be empty.")
    max_value = float('-inf')
    for num in numbers:
        if isinstance(num, (int, float)) and num > max_value:
            max_value = num
    return int(max_value)
def find_greatest_number_builtin(numbers):
    if not numbers:
        raise ValueError("Input array cannot be empty.")
    try:
        result = max(numbers, key=lambda x: float(x))
        return int(result)
    except (ValueError, TypeError):
        raise
class TestFindGreatestNumber(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(find_greatest_number([42]), 42)
    def test_multiple_elements(self):
        data = [10, -5, 3.7, 99]
        expected = int(max(data))
        result_builtin = find_greatest_number_builtin(data)
        result_custom = find_greatest_number(data)
        self.assertEqual(result_builtin, expected)
        self.assertEqual(result_custom, expected)
    def test_negative_numbers(self):
        data = [-10, -25, 0]
        expected = int(max(data))
        result_builtin = find_greatest_number_builtin(data)
        result_custom = find_greatest_number(data)
        self.assertEqual(result_builtin, expected)
        self.assertEqual(result_custom, expected)
    def test_float_precision(self):
        data = [1.0, 2.5, 3.9]
        expected = int(max(data))
        result_builtin = find_greatest_number_builtin(data)
        result_custom = find_greatest_number(data)
        self.assertEqual(result_builtin, expected)
        self.assertEqual(result_custom, expected)
    def test_empty_array(self):
        with self.assertRaises(ValueError):
            find_greatest_number([])
if __name__ == '__main__':
    unittest.main()