import unittest
INDEX_OUT_OF_BOUNDS_MESSAGE = 'Index out of bounds'

def fetch_tuple_element(data: tuple, index: int) -> any:
    if not isinstance(index, int):
        raise TypeError('Index must be an integer')
    if index < 0 or index >= len(data):
        raise IndexError(INDEX_OUT_OF_BOUNDS_MESSAGE)
    return data[index]

class TestFetchTupleElement(unittest.TestCase):

    def setUp(self):
        self.sample_tuple = (42, 'world', 2.718, {'key': 'value'})

    def test_fetch_valid_index(self):
        self.assertEqual(fetch_tuple_element(self.sample_tuple, 0), 42)
        self.assertEqual(fetch_tuple_element(self.sample_tuple, 1), 'world')
        self.assertEqual(fetch_tuple_element(self.sample_tuple, 3), {'key': 'value'})

    def test_fetch_out_of_bounds_high(self):
        with self.assertRaisesRegex(IndexError, INDEX_OUT_OF_BOUNDS_MESSAGE):
            fetch_tuple_element(self.sample_tuple, 4)

    def test_fetch_out_of_bounds_low(self):
        with self.assertRaisesRegex(IndexError, INDEX_OUT_OF_BOUNDS_MESSAGE):
            fetch_tuple_element(self.sample_tuple, -1)
if __name__ == '__main__':
    try:
        result = fetch_tuple_element((100, 200, 300), 1)
        print(result)
    except Exception as e:
        print(f'Error: {e}')
    unittest.main(argv=[''], exit=False)