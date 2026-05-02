import unittest
def find_first_element(data):
    if not data:
        return None
    return data[0]
class TestFindFirstElement(unittest.TestCase):
    def test_mixed_types(self):
        list_with_strings_and_floats = ["apple", 3.14, "banana"]
        self.assertEqual(find_first_element(list_with_strings_and_floats), "apple")
        list_with_floats_and_strings = [1.0, "hello", 2.5]
        self.assertEqual(find_first_element(list_with_floats_and_strings), 1.0)
        list_with_only_floats = [1.5, 2.7]
        self.assertEqual(find_first_element(list_with_only_floats), 1.5)
        list_with_only_strings = ["a", "b", "c"]
        self.assertEqual(find_first_element(list_with_only_strings), "a")
        empty_list = []
        self.assertIsNone(find_first_element(empty_list))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)