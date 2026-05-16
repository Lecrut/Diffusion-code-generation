import unittest
def fetch_tuple_element(data: tuple, index: int) -> any:
    if not isinstance(data, tuple):
        raise TypeError("Input must be a tuple")
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if not (0 <= index < len(data)):
        raise IndexError("Index out of bounds")
    return data[index]
class TestFetchTupleElement(unittest.TestCase):
    def test_fetch_valid_index(self):
        sample_tuple = (10, 20, 30, 40)
        self.assertEqual(fetch_tuple_element(sample_tuple, 0), 10)
        self.assertEqual(fetch_tuple_element(sample_tuple, 2), 30)
        self.assertEqual(fetch_tuple_element(sample_tuple, 3), 40)
    def test_fetch_first_element(self):
        sample_tuple = ('a', 'b', 'c')
        self.assertEqual(fetch_tuple_element(sample_tuple, 0), 'a')
    def test_fetch_last_element(self):
        sample_tuple = (5, 10, 15)
        self.assertEqual(fetch_tuple_element(sample_tuple, 2), 15)
    def test_fetch_index_out_of_bounds(self):
        sample_tuple = (1, 2)
        with self.assertRaisesRegex(IndexError, "Index out of bounds"):
            fetch_tuple_element(sample_tuple, 2)
        with self.assertRaisesRegex(IndexError, "Index out of bounds"):
            fetch_tuple_element(sample_tuple, -1)
    def test_fetch_invalid_data_type(self):
        with self.assertRaisesRegex(TypeError, "Input must be a tuple"):
            fetch_tuple_element([1, 2, 3], 0)
        with self.assertRaisesRegex(TypeError, "Input must be a tuple"):
            fetch_tuple_element("not a tuple", 0)
    def test_fetch_invalid_index_type(self):
        sample_tuple = (1, 2, 3)
        with self.assertRaisesRegex(TypeError, "Index must be an integer"):
            fetch_tuple_element(sample_tuple, 1.5)
        with self.assertRaisesRegex(TypeError, "Index must be an integer"):
            fetch_tuple_element(sample_tuple, "a")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)