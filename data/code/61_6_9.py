from typing import Tuple, Any

def fetch_element_from_tuple(data: Tuple[Any], index: int) -> Any:
    return data[index]
import unittest

class TestFetchElementFromTuple(unittest.TestCase):

    def test_fetch_element(self):
        self.assertEqual(fetch_element_from_tuple((1, 2, 3), 0), 1)
        self.assertEqual(fetch_element_from_tuple(('a', 'b', 'c'), 2), 'c')

    def test_index_out_of_range(self):
        with self.assertRaises(IndexError):
            fetch_element_from_tuple((1, 2, 3), 5)
if __name__ == '__main__':
    sample_data = (10, 20, 30, 40)
    index_to_fetch = 2
    result = fetch_element_from_tuple(sample_data, index_to_fetch)
    print(result)
    unittest.main(argv=[''], exit=False)