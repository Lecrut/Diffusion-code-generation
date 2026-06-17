import unittest
class ListAnalyzer:
    def find_min_max(self, data):
        if not data:
            return None, None
        minimum = data[0]
        maximum = data[0]
        for item in data:
            if item < minimum:
                minimum = item
            if item > maximum:
                maximum = item
        return minimum, maximum
class TestListAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = ListAnalyzer()
    def test_positive_numbers(self):
        data = [3, 1, 4, 1, 5, 9, 2]
        min_val, max_val = self.analyzer.find_min_max(data)
        self.assertEqual(min_val, 1)
        self.assertEqual(max_val, 9)
    def test_mixed_numbers(self):
        data = [10, -5, 0, 20, -100]
        min_val, max_val = self.analyzer.find_min_max(data)
        self.assertEqual(min_val, -100)
        self.assertEqual(max_val, 20)
    def test_all_same_numbers(self):
        data = [7, 7, 7, 7]
        min_val, max_val = self.analyzer.find_min_max(data)
        self.assertEqual(min_val, 7)
        self.assertEqual(max_val, 7)
    def test_empty_list(self):
        data = []
        min_val, max_val = self.analyzer.find_min_max(data)
        self.assertIsNone(min_val)
        self.assertIsNone(max_val)
    def test_single_element(self):
        data = [42]
        min_val, max_val = self.analyzer.find_min_max(data)
        self.assertEqual(min_val, 42)
        self.assertEqual(max_val, 42)
    def test_negative_numbers(self):
        data = [-10, -5, -20, -1]
        min_val, max_val = self.analyzer.find_min_max(data)
        self.assertEqual(min_val, -20)
        self.assertEqual(max_val, -1)
    def test_zero_and_negatives(self):
        data = [-5, 0, -10]
        min_val, max_val = self.analyzer.find_min_max(data)
        self.assertEqual(min_val, -10)
        self.assertEqual(max_val, 0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)