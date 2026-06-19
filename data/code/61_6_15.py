import unittest

class TupleElementFetcher:
    INDEX_OUT_OF_BOUNDS = 'Index out of bounds'

    @staticmethod
    def fetch_element(data: tuple, index: int) -> any:
        if not isinstance(data, tuple):
            raise TypeError('Input must be a tuple')
        if not isinstance(index, int):
            raise TypeError('Index must be an integer')
        if not 0 <= index < len(data):
            raise IndexError(TupleElementFetcher.INDEX_OUT_OF_BOUNDS)
        return data[index]

class TestTupleElementFetcher(unittest.TestCase):

    def test_fetch_valid_index(self):
        sample_tuple = (10, 20, 30, 40)
        self.assertEqual(TupleElementFetcher.fetch_element(sample_tuple, 0), 10)
        self.assertEqual(TupleElementFetcher.fetch_element(sample_tuple, 2), 30)
        self.assertEqual(TupleElementFetcher.fetch_element(sample_tuple, 3), 40)

    def test_fetch_out_of_bounds_high(self):
        sample_tuple = (10, 20, 30)
        with self.assertRaisesRegex(IndexError, TupleElementFetcher.INDEX_OUT_OF_BOUNDS):
            TupleElementFetcher.fetch_element(sample_tuple, 3)

    def test_fetch_out_of_bounds_negative(self):
        sample_tuple = ('a', 'b', 'c')
        with self.assertRaisesRegex(IndexError, TupleElementFetcher.INDEX_OUT_OF_BOUNDS):
            TupleElementFetcher.fetch_element(sample_tuple, -1)
if __name__ == '__main__':
    my_tuple = (5, 10, 15)
    index_to_fetch = 1
    try:
        result = TupleElementFetcher.fetch_element(my_tuple, index_to_fetch)
        print(result)
    except Exception as e:
        print(e)
    unittest.main(argv=[''], exit=False)