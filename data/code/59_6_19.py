import unittest

def find_middle_item(sequence):
    if not sequence:
        raise ValueError('The sequence is empty')
    middle_index = len(sequence) // 2
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

    def test_single_element(self):
        self.assertEqual(find_middle_item([42]), 42)
        self.assertEqual(find_middle_item(['x']), 'x')

    def test_empty_sequence(self):
        with self.assertRaises(ValueError):
            find_middle_item([])
if __name__ == '__main__':
    sequences = [[1, 2, 3, 4, 5], [10, 20, 30, 40], ['a', 'b', 'c', 'd'], [100]]
    for seq in sequences:
        try:
            print(f'Middle item of {seq}: {find_middle_item(seq)}')
        except ValueError as e:
            print(f'Error for sequence {seq}: {e}')
    unittest.main(argv=[''], exit=False)