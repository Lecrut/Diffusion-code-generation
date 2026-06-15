import unittest
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
class TestDivide(unittest.TestCase):
    def test_successful_division(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(7, 3), 2.3333333333333335)
        self.assertEqual(divide(-10, 5), -2.0)
        self.assertEqual(divide(0, 5), 0.0)
    def test_division_by_zero(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            divide(10, 0)
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            divide(0, 0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)