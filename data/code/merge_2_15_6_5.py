import unittest
def sort_array(arr):
    return sorted(arr)
class TestSortArray(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(sort_array([5, 2, 8, 1]), [1, 2, 5, 8])
    def test_negative_numbers(self):
        self.assertEqual(sort_array([-3, -1, -4, 0]), [-4, -3, -1, 0])
    def test_zeros_only(self):
        self.assertEqual(sort_array([0, 0, 5, -2, 0]), [-2, 0, 0, 0, 5])
    def test_duplicates(self):
        self.assertEqual(sort_array([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])
    def test_single_element(self):
        self.assertEqual(sort_array([42]), [42])
    def test_empty_list(self):
        self.assertEqual(sort_array([]), [])
    def test_unordered_mixed_types_integers_only(self):
        input_data = [-10, 5, -3, 0, 7]
        expected_output = sorted(input_data)
        result = sort_array(input_data)
        self.assertEqual(result, expected_output)
if __name__ == '__main__':
    unittest.main()