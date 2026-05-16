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
        data = [1]
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, [1])
    def test_simple_reversal(self):
        data = [1, 2, 3, 4, 5]
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, [5, 4, 3, 2, 1])
    def test_reversal_with_duplicates(self):
        data = [1, 2, 2, 3, 1]
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, [1, 3, 2, 2, 1])
    def test_reverse_with_negatives(self):
        data = [-1, 0, 5, -10]
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, [-10, 5, 0, -1])
    def test_list_with_strings(self):
        data = ["a", "b", "c", "d"]
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, ["d", "c", "b", "a"])
    def test_list_with_mixed_types(self):
        data = [1, "two", 3.0, False]
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, [False, 3.0, "two", 1])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)