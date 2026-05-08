import unittest
class ListReversalTest(unittest.TestCase):
    def test_empty_list(self):
        data = []
        reversal_function(data)
        self.assertEqual(data, [])
    def test_single_element(self):
        data = [1]
        reversal_function(data)
        self.assertEqual(data, [1])
    def test_simple_reversal(self):
        data = [1, 2, 3, 4]
        reversal_function(data)
        self.assertEqual(data, [4, 3, 2, 1])
    def test_list_with_duplicates(self):
        data = [1, 2, 2, 3, 1]
        reversal_function(data)
        self.assertEqual(data, [1, 3, 2, 2, 1])
    def test_list_with_negatives(self):
        data = [-1, 0, 5, -10]
        reversal_function(data)
        self.assertEqual(data, [-10, 5, 0, -1])
    def test_list_with_strings(self):
        data = ['a', 'b', 'c', 'd']
        reversal_function(data)
        self.assertEqual(data, ['d', 'c', 'b', 'a'])
def reversal_function(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)