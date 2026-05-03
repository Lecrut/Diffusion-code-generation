import unittest
def find_middle(sequence):
    n = len(sequence)
    if n == 0:
        raise ValueError("Sequence cannot be empty")
    middle_index = n // 2
    return sequence[middle_index]
class TestFindMiddle(unittest.TestCase):
    def test_odd_length(self):
        sequence = [1, 2, 3, 4, 5]
        self.assertEqual(find_middle(sequence), 3)
        sequence_long = [10, 20, 30, 40, 50, 60, 70]
        self.assertEqual(find_middle(sequence_long), 40)
    def test_even_length(self):
        sequence = [1, 2, 3, 4]
        self.assertEqual(find_middle(sequence), 2)
        sequence_long = [10, 20, 30, 40, 50, 60]
        self.assertEqual(find_middle(sequence_long), 30)
    def test_single_element(self):
        sequence = [99]
        self.assertEqual(find_middle(sequence), 99)
    def test_empty_sequence(self):
        with self.assertRaises(ValueError):
            find_middle([])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)