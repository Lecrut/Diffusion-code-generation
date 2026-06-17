import unittest
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
class TestDivideFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertAlmostEqual(divide(10, 3), 3.3333333333333335)
    def test_division_by_zero(self):
        with self.assertRaisesRegex(ZeroDivisionError, "Cannot divide by zero"):
            divide(10, 0)
        with self.assertRaisesRegex(ZeroDivisionError, "Cannot divide by zero"):
            divide(-5, 0)
    def test_negative_dividend(self):
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)
    def test_negative_divisor(self):
        self.assertEqual(divide(10, -2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)
    def test_zero_as_dividend(self):
        self.assertEqual(divide(0, 5), 0.0)
        self.assertEqual(divide(0, -5), 0.0)
    def test_both_zero(self):
        with self.assertRaisesRegex(ZeroDivisionError, "Cannot divide by zero"):
            divide(0, 0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)