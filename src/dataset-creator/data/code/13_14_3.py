import unittest
def find_greatest_number(numbers):
    if not numbers:
        raise ValueError("Input array must contain at least one element.")
    max_value = float('-inf')
    for num in numbers:
        is_numeric = isinstance(num, (int, float)) and not isinstance(num, bool)
        if not is_numeric:
            continue
        try:
            numeric_val = float(num)
            if numeric_val > max_value:
                max_value = numeric_val
        except ValueError:
            pass
    return int(max_value)
def calculate_greatest_number(numbers):
    try:
        return max(int(num) for num in numbers if isinstance(num, (int, float)) and not isinstance(num, bool))
    except ValueError:
        raise ValueError("Input array must contain at least one numeric element.")
class TestGreatestNumber(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(calculate_greatest_number([42]), 42)
    def test_multiple_elements(self):
        self.assertEqual(calculate_greatest_number([-5, 10, -3, 7]), 10)
    def test_mixed_types_filtered(self):
        self.assertEqual(find_greatest_number(['a', 'b', 5.5, 6]), int(6))
    def test_all_non_numeric(self):
        with self.assertRaises(ValueError):
            calculate_greatest_number([None, "string", True])
    def test_negative_numbers(self):
        self.assertEqual(calculate_greatest_number([-100, -200, -50]), -50)
if __name__ == '__main__':
    unittest.main()