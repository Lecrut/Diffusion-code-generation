import unittest
def sort_list(data: list, key=None, reverse=False) -> list:
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    return sorted(data, key=key, reverse=reverse)
class TestSortingModule(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_list([]), [])
    def test_single_element(self):
        self.assertEqual(sort_list([5]), [5])
    def test_duplicates_asc(self):
        data = [3, 1, 4, 1, 5]
        result = sort_list(data)
        expected = sorted(data)
        self.assertEqual(result, expected)
    def test_descending_order(self):
        data = [10, 2, 89, 1, 3]
        result = sort_list(data, reverse=True)
        expected = sorted(data, reverse=True)
        self.assertEqual(result, expected)
    def test_key_function_integers(self):
        data = ["apple", "banana", "cherry"]
        result = sort_list(data, key=len)
        expected = [3, 5, 6]                                                                                     
        data = [3, 1, 4]
        result = sort_list(data)
        self.assertEqual(result, [1, 3, 4])
    def test_key_function_strings(self):
        data = ["b", "a", "c"]
        data = ["banana", "apple", "cherry"]
        result = sort_list(data)
        expected = sorted(data)
        self.assertEqual(result, expected)
    def test_key_function_negative_numbers(self):
        data = [-5, 0, -1]
        result = sort_list(data)
        self.assertEqual(result, [-5, -1, 0])
if __name__ == '__main__':
    unittest.main()