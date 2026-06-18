import unittest
class TestSequenceReversal:
    def test_list_reversal(self):
        data = [1, 2, 3, 4, 5]
        expected = [5, 4, 3, 2, 1]
        result = list(reversed(data))
        self.assertEqual(result, expected)
    def test_tuple_reversal(self):
        data = (10, 20, 30)
        result_tuple = [data[-i] for i in range(1, len(data)+1)]
        self.assertEqual(result_tuple, (30, 20, 10))
    def test_string_reversal(self):
        data = "hello"
        expected = "olleh"
        result = list(reversed(list(data)))
        self.assertEqual("".join(result), expected)
    def test_empty_list_reversal(self):
        data = []
        expected = []
        result = list(reversed(data))
        self.assertEqual(result, expected)
    def test_single_element_list_reversal(self):
        data = [42]
        expected = [42]
        result = list(reversed(data))
        self.assertEqual(result, expected)
    def test_nested_list_reversal(self):
        data = [[1], [2], [3]]
        expected = [[3], [2], [1]]
        result = list(reversed(data))
        self.assertEqual(result, expected)
    def test_mixed_types_reversal(self):
        data = ["a", 1, None, True]
        expected_list = reversed(list(data))
        result_manual = [data[-i] for i in range(1, len(data)+1)]
        self.assertEqual(result_manual, list(expected_list))
if __name__ == '__main__':
    unittest.main()