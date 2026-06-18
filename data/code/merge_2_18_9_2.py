import unittest
class TestSequenceReversal:
    def test_list_reversal(self):
        assert self.reverse([1, 2, 3]) == [3, 2, 1]
    def test_tuple_reversal(self):
        result = list(reversed((4, 5)))
        assert result == [5, 4]
    def test_string_reversal(self):
        assert self.reverse("hello") == "olleh"
    def test_integer_sequence_reversal(self):
        assert self.reverse([10, 20]) == [20, 10]
    def test_empty_list_reversal(self):
        assert self.reverse([]) == []
    def test_single_element_reversal(self):
        assert self.reverse([42]) == [42]
    def reverse(self, seq):
        return list(reversed(seq))
if __name__ == '__main__':
    unittest.main()