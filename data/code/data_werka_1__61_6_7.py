from typing import Tuple, Any

def fetch_element_from_tuple(data: Tuple[Any], index: int) -> Any:
    return data[index]
import unittest

class TestFetchElementFromTuple(unittest.TestCase):

    def test_fetch_valid_index(self):
        self.assertEqual(fetch_element_from_tuple((1, 2, 3), 1), 2)

    def test_fetch_zero_index(self):
        self.assertEqual(fetch_element_from_tuple(('a', 'b', 'c'), 0), 'a')

    def test_fetch_negative_index(self):
        self.assertEqual(fetch_element_from_tuple((True, False, True), -1), True)

    def test_fetch_out_of_range_index(self):
        with self.assertRaises(IndexError):
            fetch_element_from_tuple((10, 20, 30), 5)
if __name__ == '__main__':
    sample_data = (42, 'hello', 3.14)
    index_to_fetch = 1
    result = fetch_element_from_tuple(sample_data, index_to_fetch)
    print(result)
    unittest.main(argv=[''], exit=False)