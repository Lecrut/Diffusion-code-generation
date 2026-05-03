import unittest
def find_first_element(data):
    if not data:
        return None
    return data[0]
class TestFindFirstElement(unittest.TestCase):
    def test_mixed_types(self):
        list_with_strings_and_floats = ["apple", 3.14, "banana"]
        self.assertEqual(find_first_element(list_with_strings_and_floats), "apple")
        list_with_floats = [1.0, 2.5, 3.0]
        self.assertEqual(find_first_element(list_with_floats), 1.0)
        list_with_strings = ["hello", "world", "test"]
        self.assertEqual(find_first_element(list_with_strings), "hello")
        list_with_floats_and_strings = [5.5, "a", 10.0]
        self.assertEqual(find_first_element(list_with_floats_and_strings), 5.5)
        empty_list = []
        self.assertIsNone(find_first_element(empty_list))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)