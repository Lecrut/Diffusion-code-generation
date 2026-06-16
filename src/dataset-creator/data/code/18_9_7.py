import unittest
class TestSequenceReversal:
    def test_list_reversal(self):
        self.assertEqual(list(reversed([1, 2, 3])), [3, 2, 1])
    def test_tuple_reversal(self):
        original = (4, 5)
        reversed_val = list(reversed(original))
        self.assertEqual(reversed_val, [5, 4])
    def test_string_reversal(self):
        self.assertEqual(list(reversed("hello")), ['o', 'l', 'l', 'e', 'h'])
    def test_empty_list_reversal(self):
        self.assertEqual(list(reversed([])), [])
    def test_single_element_list_reversal(self):
        self.assertEqual(list(reversed([42])), [42])
    def test_nested_structure_reversal(self):
        data = [[1, 2], [3]]
        reversed_data = list(reversed(data))
        self.assertEqual(reversed_data, [[3], [1, 2]])
if __name__ == '__main__':
    unittest.main()