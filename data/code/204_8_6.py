import unittest
class ListMiddleCalculator:
    def find_middle(self, data):
        if not data:
            return None
        n = len(data)
        if n % 2 == 1:
            middle_index = n // 2
            return data[middle_index]
        else:
            middle_right_index = n // 2
            middle_left_index = middle_right_index - 1
            return (data[middle_left_index] + data[middle_right_index]) / 2
class TestListMiddleCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ListMiddleCalculator()
    def test_empty_list(self):
        self.assertIsNone(self.calculator.find_middle([]))
    def test_single_element(self):
        self.assertEqual(self.calculator.find_middle([5]), 5)
    def test_odd_length(self):
        self.assertEqual(self.calculator.find_middle([1, 2, 3, 4, 5]), 3)
        self.assertEqual(self.calculator.find_middle([1, 2, 10, 4, 5]), 10)
    def test_even_length(self):
        self.assertAlmostEqual(self.calculator.find_middle([1, 2, 3, 4]), 2.5)
        self.assertAlmostEqual(self.calculator.find_middle([10, 20, 30, 40]), 25.0)
    def test_even_length_with_floats(self):
        self.assertAlmostEqual(self.calculator.find_middle([1.5, 2.5]), 2.0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)