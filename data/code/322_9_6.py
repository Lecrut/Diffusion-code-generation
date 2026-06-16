import unittest
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
class TestDivideFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertAlmostEqual(divide(10, 3), 3.3333333333333335)
    def test_division_by_one(self):
        self.assertEqual(divide(7, 1), 7.0)
        self.assertEqual(divide(-5, 1), -5.0)
    def test_division_resulting_in_zero(self):
        self.assertEqual(divide(0, 5), 0.0)
        self.assertEqual(divide(-10, 0), None)                                                                                               
    def test_division_by_zero(self):
        with self.assertRaisesRegex(ZeroDivisionError, "Cannot divide by zero"):
            divide(10, 0)
        with self.assertRaisesRegex(ZeroDivisionError, "Cannot divide by zero"):
            divide(-5, 0)
    def test_negative_numbers_result_positive(self):
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(10, -2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)
    def test_division_with_floats(self):
        self.assertAlmostEqual(divide(10.0, 3.0), 3.3333333333333335)
        self.assertAlmostEqual(divide(1.0, 4.0), 0.25)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)