import unittest
class ReverseSequenceTests(unittest.TestCase):
    def test_list_reversal(self):
        self.assertEqual(list(reversed([1, 2, 3])), [3, 2, 1])
    def test_tuple_reversal(self):
        result = list(reversed((4, 5)))
        self.assertEqual(result, [5, 4])
    def test_string_reversal(self):
        self.assertEqual(list(reversed("hello")), ['o', 'l', 'l', 'e', 'h'])
    def test_empty_list(self):
        self.assertEqual(list(reversed([])), [])
    def test_single_element_list(self):
        self.assertEqual(list(reversed([42])), [42])
    def test_nested_structure_reversal(self):
        data = [[1, 2], [3]]
        result = list(reversed(data))
        self.assertEqual(result, [[3], [1, 2]])
if __name__ == '__main__':
    unittest.main()