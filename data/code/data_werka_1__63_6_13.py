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
    sample_values = [
        [],
        ['apple', 'banana', 'cherry'],
        [1.1, 2.2, 3.3],
        ['apple', 1.1, 'banana']
    ]
    
    for value in sample_values:
        print(find_first_element(value))