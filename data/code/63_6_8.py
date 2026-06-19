import unittest

def find_first_element(lst):
    if not lst:
        return None
    return lst[0]

class TestFindFirstElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(find_first_element([]))

    def test_string_list(self):
        self.assertEqual(find_first_element(['apple', 'banana', 'cherry']), 'apple')

    def test_float_list(self):
        self.assertEqual(find_first_element([1.1, 2.2, 3.3]), 1.1)

    def test_mixed_list(self):
        self.assertEqual(find_first_element(['apple', 1.1, 'banana']), 'apple')
if __name__ == '__main__':
    sample_string_list = ['apple', 'banana', 'cherry']
    sample_float_list = [1.1, 2.2, 3.3]
    sample_mixed_list = ['apple', 1.1, 'banana']
    print(find_first_element(sample_string_list))
    print(find_first_element(sample_float_list))
    print(find_first_element(sample_mixed_list))
    unittest.main(argv=[''], exit=False)