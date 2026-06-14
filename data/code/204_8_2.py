import unittest
def calculate_middle(data):
    if not data:
        raise ValueError("List cannot be empty")
    n = len(data)
    if n % 2 == 1:
        middle_index = n // 2
        return data[middle_index]
    else:
        middle_index_right = n // 2
        middle_index_left = middle_index_right - 1
        return data[middle_index_left]
class TestMiddleValue(unittest.TestCase):
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_middle([])
    def test_single_element(self):
        self.assertEqual(calculate_middle([5]), 5)
    def test_odd_length(self):
        self.assertEqual(calculate_middle([1, 2, 3, 4, 5]), 3)
        self.assertEqual(calculate_middle([10, 20, 30]), 20)
    def test_even_length(self):
        self.assertEqual(calculate_middle([1, 2, 3, 4]), 2)
        self.assertEqual(calculate_middle([10, 20, 30, 40]), 20)
    def test_two_elements(self):
        self.assertEqual(calculate_middle([5, 10]), 5)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)