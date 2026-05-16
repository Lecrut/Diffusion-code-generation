import unittest
class ListReverser:
    def reverse_in_place(self, data):
        left = 0
        right = len(data) - 1
        while left < right:
            data[left], data[right] = data[right], data[left]
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
    def test_simple_list(self):
        data = [1, 2, 3, 4]
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, [4, 3, 2, 1])
    def test_list_with_duplicates(self):
        data = [5, 2, 8, 2, 5]
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, [5, 2, 8, 2, 5])
    def test_list_with_negatives(self):
        data = [-1, 0, 5, -10]
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, [-10, 5, 0, -1])
    def test_list_with_strings(self):
        data = ["a", "b", "c", "d"]
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, ["d", "c", "b", "a"])
    def test_longer_list(self):
        data = [10, 20, 30, 40, 50, 60]
        self.reverser.reverse_in_place(data)
        self.assertEqual(data, [60, 50, 40, 30, 20, 10])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)