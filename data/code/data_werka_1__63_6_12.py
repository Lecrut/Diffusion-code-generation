import unittest

def find_first_element(data):
    if not data:
        return None
    return data[0]

class TestFindFirstElement(unittest.TestCase):

    def test_mixed_types(self):
        list_with_strings_and_floats = ['apple', 3.14, 'banana']
        self.assertEqual(find_first_element(list_with_strings_and_floats), 'apple')
        list_with_floats_and_strings = [1.0, 'hello', 2.5]
        self.assertEqual(find_first_element(list_with_floats_and_strings), 1.0)
        list_with_only_strings = ['a', 'b', 'c']
        self.assertEqual(find_first_element(list_with_only_strings), 'a')
        list_with_only_floats = [1.1, 2.2, 3.3]
        self.assertEqual(find_first_element(list_with_only_floats), 1.1)
        empty_list = []
        self.assertIsNone(find_first_element(empty_list))
if __name__ == '__main__':
    sample_list_1 = ['apple', 3.14, 'banana']
    sample_list_2 = [1.0, 'hello', 2.5]
    sample_list_3 = ['a', 'b', 'c']
    sample_list_4 = [1.1, 2.2, 3.3]
    empty_sample_list = []
    print(find_first_element(sample_list_1))
    print(find_first_element(sample_list_2))
    print(find_first_element(sample_list_3))
    print(find_first_element(sample_list_4))
    print(find_first_element(empty_sample_list))
    unittest.main(argv=[''], exit=False)