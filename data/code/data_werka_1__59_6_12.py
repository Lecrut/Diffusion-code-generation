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
    try:
        sequence1 = [1, 2, 3, 4, 5]
        sequence2 = [10, 20, 30, 40]
        sequence3 = ['a', 'b', 'c', 'd']
        sequence4 = [100]
        print(find_middle_item(sequence1))
        print(find_middle_item(sequence2))
    except ValueError as e:
        print(e)
    unittest.main(argv=[''], exit=False)