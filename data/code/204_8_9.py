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
            middle_right_index = n // 2
            middle_left_index = middle_right_index - 1
            return (data[middle_left_index] + data[middle_right_index]) / 2
class TestListMiddleCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ListMiddleCalculator()
    def test_empty_list(self):
        data = []
        result = self.calculator.find_middle(data)
        self.assertIsNone(result)
    def test_single_element(self):
        data = [5]
        result = self.calculator.find_middle(data)
        self.assertEqual(result, 5)
    def test_odd_length(self):
        data = [1, 2, 3, 4, 5]
        result = self.calculator.find_middle(data)
        self.assertEqual(result, 3)
    def test_odd_length_larger(self):
        data = [10, 20, 30, 40, 50]
        result = self.calculator.find_middle(data)
        self.assertEqual(result, 30)
    def test_even_length(self):
        data = [1, 2, 3, 4]
        result = self.calculator.find_middle(data)
        self.assertAlmostEqual(result, 2.5)
    def test_even_length_larger(self):
        data = [10, 20, 30, 40]
        result = self.calculator.find_middle(data)
        self.assertAlmostEqual(result, 25.0)
    def test_even_length_floats(self):
        data = [1, 10, 11, 20]
        result = self.calculator.find_middle(data)
        self.assertAlmostEqual(result, 10.5)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-action', 'excec'], exit=False)