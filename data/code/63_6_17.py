import unittest

def find_first_element(lst):
    if not lst:
        return None
    return lst[0]

class TestFindFirstElement(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(find_first_element([]))

    def test_list_with_strings(self):
        self.assertEqual(find_first_element(['apple', 'banana', 'cherry']), 'apple')

    def test_list_with_floats(self):
        self.assertEqual(find_first_element([1.1, 2.2, 3.3]), 1.1)

    def test_list_with_mixed_types(self):
        self.assertEqual(find_first_element(['apple', 1.1, True]), 'apple')

if __name__ == '__main__':
    sample_values = ['apple', 1.1, True]
    print(find_first_element(sample_values))
    unittest.main(argv=[''], exit=False)