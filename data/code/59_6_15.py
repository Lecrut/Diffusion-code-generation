import unittest

def find_middle_item(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError("The sequence is empty")
    middle_index = length // 2
    return sequence[middle_index]

class TestFindMiddleItem(unittest.TestCase):
    def test_odd_length(self):
        self.assertEqual(find_middle_item([1, 2, 3]), 2)
        self.assertEqual(find_middle_item(['a', 'b', 'c']), 'b')
    
    def test_even_length(self):
        self.assertEqual(find_middle_item([1, 2, 3, 4]), 3)
        self.assertEqual(find_middle_item(['a', 'b', 'c', 'd']), 'c')
    
    def test_single_element(self):
        self.assertEqual(find_middle_item([42]), 42)
        self.assertEqual(find_middle_item(['x']), 'x')
    
    def test_empty_sequence(self):
        with self.assertRaises(ValueError):
            find_middle_item([])

if __name__ == '__main__':
    sample_odd = [1, 2, 3, 4, 5]
    sample_even = [10, 20, 30, 40]
    print("Middle of odd sequence:", find_middle_item(sample_odd))
    print("Middle of even sequence:", find_middle_item(sample_even))