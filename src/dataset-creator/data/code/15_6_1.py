import unittest
def sort_array(arr):
    return sorted(arr)
class TestSortingLogic(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(sort_array([5, 2, 8, 1]), [1, 2, 5, 8])
    def test_negative_numbers(self):
        self.assertEqual(sort_array([-3, -10, 0, 5]), [-10, -3, 0, 5])
    def test_zeros_and_negatives(self):
        self.assertEqual(sort_array([0, -5, 0, -2]), [-5, -2, 0, 0])
    def test_duplicates(self):
        input_list = [4, 1, 6, 3, 7, 9, 8]
        expected_output = sorted(input_list)
        self.assertEqual(sort_array(input_list), expected_output)
    def test_empty_list(self):
        self.assertEqual(sort_array([]), [])
if __name__ == '__main__':
    unittest.main()