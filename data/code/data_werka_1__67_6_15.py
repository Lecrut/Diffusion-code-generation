import unittest

class Calculator:
    def sum_two_numbers(self, a, b):
        return a + b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum_positive_numbers(self):
        self.assertEqual(self.calc.sum_two_numbers(3, 4), 7)

    def test_sum_negative_numbers(self):
        self.assertEqual(self.calc.sum_two_numbers(-1, -2), -3)

    def test_sum_mixed_numbers(self):
        self.assertEqual(self.calc.sum_two_numbers(-1, 2), 1)

    def test_sum_zero(self):
        self.assertEqual(self.calc.sum_two_numbers(0, 0), 0)

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.sum_two_numbers(5, 7)
    result2 = calc.sum_two_numbers(-3, 8)
    print(result1)
    print(result2)
    unittest.main(argv=[''], exit=False)