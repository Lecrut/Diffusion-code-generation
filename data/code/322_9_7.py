import unittest
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
class TestDivideFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertAlmostEqual(divide(7, 3), 2.3333333333333335)
    def test_division_by_one(self):
        self.assertEqual(divide(15, 1), 15.0)
        self.assertEqual(divide(-8, 1), -8.0)
    def test_division_resulting_in_zero(self):
        self.assertEqual(divide(0, 5), 0.0)
        self.assertEqual(divide(-10, 0), None)                                                                   
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
        with self.assertRaises(ZeroDivisionError):
            divide(-5, 0)
    def test_negative_dividend(self):
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(10, -2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)
    def test_floating_point_results(self):
        self.assertAlmostEqual(divide(1, 3), 0.3333333333333333)
        self.assertAlmostEqual(divide(5, 2), 2.5)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)