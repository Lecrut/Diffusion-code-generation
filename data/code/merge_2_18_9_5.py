import unittest
class ReverseSequenceTests(unittest.TestCase):
    def test_reverse_list_basic(self):
        self.assertEqual(list(reversed([1, 2, 3])), [3, 2, 1])
    def test_reverse_tuple_basic(self):
        result = list(reversed((4, 5)))
        self.assertEqual(result, [5, 4])
    def test_reverse_string_basic(self):
        self.assertEqual(list(reversed("hello")), ['o', 'l', 'l', 'e', 'h'])
    def test_reverse_empty_list(self):
        self.assertEqual(list(reversed([])), [])
    def test_reverse_single_element_list(self):
        self.assertEqual(list(reversed([42])), [42])
    def test_reverse_nested_structure(self):
        data = [[1, 2], [3]]
        expected = [[[3], [2, 1]], []]
        self.assertEqual(list(reversed(data)), [[3], [1, 2]])
    def test_reverse_mixed_types(self):
        data = ['a', 'b', {'key': 'val'}, None]
        expected = [None, {'key': 'val'}, 'b', 'a']
        self.assertEqual(list(reversed(data)), expected)
if __name__ == '__main__':
    unittest.main()