import unittest
def sort_array(arr):
    return sorted(arr)
class TestSortingLogic(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sort_array([5, 2, 8]), [2, 5, 8])
    def test_negative_numbers(self):
        self.assertEqual(sort_array([-3, -1, -9, 0]), [-9, -3, -1, 0])
    def test_zeros_and_mixed_signs(self):
        self.assertEqual(sort_array([0, -5, 0, 3, -2]), [-5, -2, 0, 0, 3])
    def test_duplicates(self):
        self.assertEqual(sort_array([4, 4, 1, 4, 1]), [1, 1, 4, 4, 4])
    def test_single_element(self):
        self.assertEqual(sort_array([42]), [42])
    def test_empty_list(self):
        self.assertEqual(sort_array([]), [])
    def test_already_sorted(self):
        self.assertEqual(sort_array([1, 2, 3, 4]), [1, 2, 3, 4])
    def test_reverse_sorted(self):
        self.assertEqual(sort_array([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
if __name__ == '__main__':
    unittest.main()