import unittest
class ListMiddleCalculator:
    def find_middle(self, data):
        if not data:
            return None
        n = len(data)
        if n % 2 != 0:
            middle_index = n // 2
            return data[middle_index]
        else:
            middle1_index = n // 2 - 1
            middle2_index = n // 2
            return (data[middle1_index] + data[middle2_index]) / 2
class TestListMiddleCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ListMiddleCalculator()
    def test_empty_list(self):
        self.assertIsNone(self.calculator.find_middle([]))
    def test_single_element(self):
        self.assertEqual(self.calculator.find_middle([5]), 5)
    def test_odd_length(self):
        self.assertEqual(self.calculator.find_middle([1, 2, 10, 4, 5]), 10)
        self.assertEqual(self.calculator.find_middle([1, 2, 3, 4, 5, 6, 7]), 4)
    def test_even_length(self):
        self.assertAlmostEqual(self.calculator.find_middle([1, 2, 10, 20]), 15.0)
        self.assertAlmostEqual(self.calculator.find_middle([1, 2, 3, 4, 40, 50]), 45.0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)