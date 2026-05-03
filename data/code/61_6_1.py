import unittest
def fetch_tuple_element(data: tuple, index: int) -> any:
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
    def test_fetch_out_of_bounds_high(self):
        sample_tuple = (10, 20, 30)
        with self.assertRaisesRegex(IndexError, "Index out of bounds"):
            fetch_tuple_element(sample_tuple, 3)
    def test_fetch_out_of_bounds_negative(self):
        sample_tuple = (10, 20, 30)
        with self.assertRaisesRegex(IndexError, "Index out of bounds"):
            fetch_tuple_element(sample_tuple, -1)
    def test_fetch_invalid_index_type(self):
        sample_tuple = (10, 20, 30)
        with self.assertRaisesRegex(TypeError, "Index must be an integer"):
            fetch_tuple_element(sample_tuple, 1.5)
        with self.assertRaisesRegex(TypeError, "Index must be an integer"):
            fetch_tuple_element(sample_tuple, "a")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)