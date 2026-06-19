import unittest

def find_middle_item(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError('The sequence is empty')
    middle_index = (length - 1) // 2
    return sequence[middle_index]

class TestFindMiddleItem(unittest.TestCase):

    def test_odd_length(self):
        self.assertEqual(find_middle_item([1, 2, 3]), 2)
        self.assertEqual(find_middle_item(['a', 'b', 'c']), 'b')

    def test_even_length(self):
        with self.assertRaises(ValueError):
            find_middle_item([1, 2, 3, 4])
        with self.assertRaises(ValueError):
            find_middle_item(['a', 'b', 'c', 'd'])

    def test_empty_sequence(self):
        with self.assertRaises(ValueError):
            find_middle_item([])
if __name__ == '__main__':
    print(find_middle_item([1, 2, 3]))
    print(find_middle_item(['a', 'b', 'c']))
    unittest.main(argv=[''], exit=False)