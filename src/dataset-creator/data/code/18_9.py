import unittest
class TestSequenceReversal:
    def test_list_reversal(self):
        self.assertEqual(list(reversed([1, 2, 3])), [3, 2, 1])
    def test_tuple_reversal(self):
        original = (5, 4, 3)
        reversed_data = list(reversed(original))
        self.assertEqual(reversed_data, [3, 4, 5])
    def test_string_reversal(self):
        s = "hello"
        expected = "olleh"
        result = "".join(reversed(s))
        self.assertEqual(result, expected)
    def test_empty_list_reversal(self):
        empty = []
        reversed_data = list(reversed(empty))
        self.assertEqual(reversed_data, [])
    def test_single_element_list_reversal(self):
        single = [42]
        reversed_data = list(reversed(single))
        self.assertEqual(reversed_data, [42])
    def test_nested_structure_reversal(self):
        nested = [[1], 2, [3]]
        reversed_data = list(reversed(nested))
        self.assertEqual(reversed_data, [[3], 2, [1]])
    def test_mixed_types_reversal(self):
        mixed = ["a", "b", None]
        result = "".join([str(x) for x in reversed(mixed)]) if isinstance(result, str) else list(reversed(mixed))
        self.assertEqual(list(reversed(mixed)), [None, 'b', 'a'])
if __name__ == '__main__':
    unittest.main()