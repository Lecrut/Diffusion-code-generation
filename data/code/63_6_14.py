import unittest

def find_first_element(data):
    if not isinstance(data, list):
        raise ValueError('Input must be a list')
    if not data:
        return None
    return data[0]

class TestFindFirstElement(unittest.TestCase):

    def test_mixed_types(self):
        mixed_list = ['apple', 3.14, 'banana']
        self.assertEqual(find_first_element(mixed_list), 'apple')

    def test_floats_and_strings(self):
        float_string_list = [1.0, 'hello', 2.5]
        self.assertEqual(find_first_element(float_string_list), 1.0)

    def test_only_strings(self):
        only_strings = ['a', 'b', 'c']
        self.assertEqual(find_first_element(only_strings), 'a')

    def test_only_floats(self):
        only_floats = [1.1, 2.2, 3.3]
        self.assertEqual(find_first_element(only_floats), 1.1)

    def test_empty_list(self):
        empty = []
        self.assertIsNone(find_first_element(empty))

    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            find_first_element('not a list')
if __name__ == '__main__':
    sample_mixed_list = ['apple', 3.14, 'banana']
    print(find_first_element(sample_mixed_list))