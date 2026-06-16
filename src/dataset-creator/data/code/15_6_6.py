import unittest
def sort_array(arr):
    return sorted(arr)
class TestSortingLogic(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sort_array([5, 2, 8]), [2, 5, 8])
    def test_negative_numbers(self):
        self.assertEqual(sort_array([-3, -1, -9]), [-9, -3, -1])
    def test_mixed_signs(self):
        self.assertEqual(sort_array([0, -4, 7, -2]), [-4, -2, 0, 7])
    def test_zeros(self):
        self.assertEqual(sort_array([5, 0, 3, 0]), [0, 0, 3, 5])
    def test_duplicates(self):
        self.assertEqual(sort_array([1, 4, 2, 2, 3, 1]), [1, 1, 2, 2, 3, 4])
    def test_single_element(self):
        self.assertEqual(sort_array([42]), [42])
    def test_empty_list(self):
        self.assertEqual(sort_array([]), [])
    def test_two_elements_unsorted(self):
        self.assertEqual(sort_array([9, 10]), [9, 10])
if __name__ == '__main__':
    unittest.main()