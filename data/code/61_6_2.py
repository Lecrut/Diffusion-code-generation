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
    def setUp(self):
        self.sample_tuple = (10, "hello", 3.14, [1, 2])
    def test_fetch_valid_index(self):
        self.assertEqual(fetch_tuple_element(self.sample_tuple, 0), 10)
        self.assertEqual(fetch_tuple_element(self.sample_tuple, 2), 3.14)
        self.assertEqual(fetch_tuple_element(self.sample_tuple, 3), [1, 2])
    def test_fetch_out_of_bounds_high(self):
        with self.assertRaisesRegex(IndexError, "Index out of bounds"):
            fetch_tuple_element(self.sample_tuple, 4)
    def test_fetch_out_of_bounds_low(self):
        with self.assertRaisesRegex(IndexError, "Index out of bounds"):
            fetch_tuple_element(self.sample_tuple, -1)
    def test_fetch_invalid_type_data(self):
        with self.assertRaisesRegex(TypeError, "Input must be a tuple"):
            fetch_tuple_element([1, 2, 3], 0)
        with self.assertRaisesRegex(TypeError, "Input must be a tuple"):
            fetch_tuple_element("not a tuple", 0)
    def test_fetch_invalid_type_index(self):
        with self.assertRaisesRegex(TypeError, "Index must be an integer"):
            fetch_tuple_element(self.sample_tuple, 1.5)
        with self.assertRaisesRegex(TypeError, "Index must be an integer"):
            fetch_tuple_element(self.sample_tuple, "a")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)