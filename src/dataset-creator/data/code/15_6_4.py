import unittest
def sort_array(arr):
    return sorted(arr)
class TestSortingLogic(unittest.TestCase):
    def test_positive_integers(self):
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
    def test_all_same_elements(self):
        self.assertEqual(sort_array([7, 7, 7, 7]), [7, 7, 7, 7])
if __name__ == '__main__':
    unittest.main()