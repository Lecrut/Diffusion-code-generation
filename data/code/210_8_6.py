import unittest
def calculate_range(data):
    if not data:
        return 0
    return max(data) - min(data)
class TestCalculateRange(unittest.TestCase):
    def test_standard_positive_numbers(self):
        data = [1, 5, 2, 8]
        self.assertEqual(calculate_range(data), 7)
    def test_list_with_negative_numbers(self):
        data = [-5, 0, 5, 10]
        self.assertEqual(calculate_range(data), 15)
    def test_list_with_mixed_numbers(self):
        data = [-10, 20, -5, 5]
        self.assertEqual(calculate_range(data), 25)
    def test_list_with_all_same_numbers(self):
        data = [3, 3, 3, 3]
        self.assertEqual(calculate_range(data), 0)
    def test_single_element_list(self):
        data = [42]
        self.assertEqual(calculate_range(data), 0)
    def test_empty_list(self):
        data = []
        self.assertEqual(calculate_range(data), 0)
    def test_list_with_only_negatives(self):
        data = [-10, -5, -20]
        self.assertEqual(calculate_range(data), 15)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)