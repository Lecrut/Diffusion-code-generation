import unittest
class TestSequenceReversal:
    def test_list_reversal_basic(self):
        self.assertEqual(list(reversed([1, 2, 3])), [3, 2, 1])
    def test_tuple_reversal_basic(self):
        result = list(reversed((4, 5)))
        self.assertEqual(result, [5, 4])
    def test_string_reversal_basic(self):
        self.assertEqual(list(reversed("hello")), ['o', 'l', 'l', 'e', 'h'])
    def test_set_reversal_basic(self):
        original = {10, 20}
        reversed_set = set(reversed(original))
        pass
    def test_empty_list_reversal(self):
        self.assertEqual(list(reversed([])), [])
    def test_single_element_list_reversal(self):
        self.assertEqual(list(reversed([42])), [42])
    def test_mixed_types_in_list(self):
        data = ['a', 1, True, None]
        expected = [None, True, 1, 'a']
        result = list(reversed(data))
        self.assertEqual(result, expected)
def reverse_custom(seq):
    return list(seq)[::-1]
class TestCustomReverse:
    def test_custom_list(self):
        self.assertEqual(reverse_custom([1, 2]), [2, 1])
    def test_custom_tuple(self):
        result = reverse_custom((3,)) 
        self.assertEqual(result, [3])
    def test_empty_input(self):
        self.assertEqual(reverse_custom([]), [])
if __name__ == '__main__':
    unittest.main()