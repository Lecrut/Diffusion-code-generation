import unittest
class ListReverser:
    def reverse_in_place(self, lst):
        left = 0
        right = len(lst) - 1
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
class TestListReverser(unittest.TestCase):
    def setUp(self):
        self.reverser = ListReverser()
    def test_empty_list(self):
        data = []
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, [])
    def test_single_element(self):
        data = [5]
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, [5])
    def test_even_length_list(self):
        data = [1, 2, 3, 4]
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, [4, 3, 2, 1])
    def test_odd_length_list(self):
        data = [10, 20, 30, 40, 50]
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, [50, 40, 30, 20, 10])
    def test_list_with_negatives(self):
        data = [-1, 0, 1, -5]
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, [-5, 1, 0, -1])
    def test_list_with_duplicates(self):
        data = [2, 2, 3, 2]
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, [2, 3, 2, 2])
    def test_list_with_strings(self):
        data = ['a', 'b', 'c', 'd']
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, ['d', 'c', 'b', 'a'])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)