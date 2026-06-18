import unittest
def sort_array(arr):
    return sorted(arr)
class TestSortingLogic(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sort_array([5, 2, 8, 1]), [1, 2, 5, 8])
    def test_negative_numbers(self):
        self.assertEqual(sort_array([-3, -10, 0, 5]), [-10, -3, 0, 5])
    def test_zeros_and_negatives(self):
        self.assertEqual(sort_array([0, -2, 0, -1]), [-2, -1, 0, 0])
    def test_duplicates(self):
        self.assertEqual(sort_array([4, 4, 3, 4, 5]), [3, 4, 4, 4, 5])
    def test_single_element(self):
        self.assertEqual(sort_array([99]), [99])
    def test_empty_list(self):
        self.assertEqual(sort_array([]), [])
    def test_all_same_elements(self):
        self.assertEqual(sort_array([7, 7, 7, 7]), [7, 7, 7, 7])
if __name__ == '__main__':
    unittest.main()