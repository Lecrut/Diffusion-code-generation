import unittest

def find_middle_item(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError('The sequence is empty')
    middle_index = length // 2
    return sequence[middle_index]

class TestFindMiddleItem(unittest.TestCase):

    def test_odd_length(self):
        self.assertEqual(find_middle_item([1, 2, 3]), 2)
        self.assertEqual(find_middle_item(['a', 'b', 'c']), 'b')

    def test_even_length(self):
        with self.assertRaises(ValueError):
            find_middle_item([1, 2])
        with self.assertRaises(ValueError):
            find_middle_item(['a', 'b'])

    def test_empty_sequence(self):
        with self.assertRaises(ValueError):
            find_middle_item([])
if __name__ == '__main__':
    odd_sequence = [1, 2, 3, 4, 5]
    even_sequence = [10, 20, 30, 40]
    empty_sequence = []
    print('Middle item of odd sequence:', find_middle_item(odd_sequence))
    try:
        print('Middle item of even sequence:', find_middle_item(even_sequence))
    except ValueError as e:
        print('Error for even sequence:', e)
    try:
        print('Middle item of empty sequence:', find_middle_item(empty_sequence))
    except ValueError as e:
        print('Error for empty sequence:', e)
    unittest.main(argv=[''], exit=False)