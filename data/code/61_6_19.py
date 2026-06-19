from typing import Tuple, Any

def fetch_element_from_tuple(data: Tuple[Any], index: int) -> Any:
    try:
        return data[index]
    except IndexError:
        raise ValueError('Index out of range')
import unittest

class TestFetchElementFromTuple(unittest.TestCase):

    def test_fetch_valid_index(self):
        self.assertEqual(fetch_element_from_tuple((1, 2, 3), 1), 2)

    def test_fetch_invalid_index(self):
        with self.assertRaises(ValueError) as context:
            fetch_element_from_tuple((1, 2, 3), 5)
        self.assertEqual(str(context.exception), 'Index out of range')
if __name__ == '__main__':
    sample_data = (10, 20, 30, 40, 50)
    index_to_fetch = 3
    result = fetch_element_from_tuple(sample_data, index_to_fetch)
    print(result)
    unittest.main(argv=[''], exit=False)