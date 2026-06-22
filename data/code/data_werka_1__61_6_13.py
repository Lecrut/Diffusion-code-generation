import unittest

def fetch_tuple_element(data: tuple, index: int) -> any:
    if not isinstance(data, tuple):
        raise TypeError('Input must be a tuple')
    if not isinstance(index, int):
        raise TypeError('Index must be an integer')
    if not 0 <= index < len(data):
        raise IndexError('Index out of bounds')
    return data[index]

class TestFetchTupleElement(unittest.TestCase):

    def test_fetch_valid_index(self):
        sample_tuple = ('apple', 'banana', 'cherry')
        self.assertEqual(fetch_tuple_element(sample_tuple, 0), 'apple')
        self.assertEqual(fetch_tuple_element(sample_tuple, 1), 'banana')
        self.assertEqual(fetch_tuple_element(sample_tuple, 2), 'cherry')

    def test_fetch_out_of_bounds_high(self):
        sample_tuple = (True, False)
        with self.assertRaisesRegex(IndexError, 'Index out of bounds'):
            fetch_tuple_element(sample_tuple, 2)

    def test_fetch_out_of_bounds_low(self):
        sample_tuple = ('one', 'two')
        with self.assertRaisesRegex(IndexError, 'Index out of bounds'):
            fetch_tuple_element(sample_tuple, -1)
if __name__ == '__main__':
    fruits = ('apple', 'banana', 'cherry')
    index_to_fetch = 1
    fetched_element = fetch_tuple_element(fruits, index_to_fetch)
    print(f'Fetched element: {fetched_element}')
    unittest.main(argv=[''], exit=False)