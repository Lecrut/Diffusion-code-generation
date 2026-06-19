import unittest

def fetch_tuple_element(data: tuple, index: int) -> any:
    if not isinstance(data, tuple):
        raise TypeError('Input must be a tuple')
    if not isinstance(index, int):
        raise TypeError('Index must be an integer')
    try:
        return data[index]
    except IndexError:
        raise IndexError('Index out of bounds')

class TestFetchTupleElement(unittest.TestCase):

    def test_fetch_valid_index(self):
        sample_tuple = (10, 20, 30, 40)
        self.assertEqual(fetch_tuple_element(sample_tuple, 0), 10)
        self.assertEqual(fetch_tuple_element(sample_tuple, 2), 30)
        self.assertEqual(fetch_tuple_element(sample_tuple, 3), 40)

    def test_fetch_out_of_bounds_high(self):
        sample_tuple = (10, 20, 30)
        with self.assertRaisesRegex(IndexError, 'Index out of bounds'):
            fetch_tuple_element(sample_tuple, 3)

    def test_fetch_out_of_bounds_negative(self):
        sample_tuple = ('a', 'b', 'c')
        with self.assertRaisesRegex(IndexError, 'Index out of bounds'):
            fetch_tuple_element(sample_tuple, -1)

    def test_invalid_input_type(self):
        sample_list = [10, 20, 30]
        with self.assertRaisesRegex(TypeError, 'Input must be a tuple'):
            fetch_tuple_element(sample_list, 0)

    def test_invalid_index_type(self):
        sample_tuple = (10, 20, 30)
        with self.assertRaisesRegex(TypeError, 'Index must be an integer'):
            fetch_tuple_element(sample_tuple, 'a')
if __name__ == '__main__':
    sample_tuple = ('x', 'y', 'z')
    print(fetch_tuple_element(sample_tuple, 1))
    unittest.main(argv=[''], exit=False)