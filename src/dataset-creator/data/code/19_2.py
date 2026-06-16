import unittest
class MathOperations:
    def add(self, a: int, b: int) -> int:
        return a + b
    def multiply(self, a: int, b: int) -> int:
        return a * b
    def divide(self, dividend: float, divisor: float) -> float:
        if divisor == 0.0:
            raise ValueError("Division by zero is not allowed.")
        return dividend / divisor
class TestMathOperations(unittest.TestCase):
    def test_add_positive_integers(self):
        result = MathOperations().add(5, 3)
        self.assertEqual(result, 8)
    def test_add_negative_numbers(self):
        result = MathOperations().add(-10, -20)
        self.assertEqual(result, -30)
    def test_multiply_zero(self):
        result = MathOperations().multiply(45, 0)
        self.assertEqual(result, 0)
    def test_divide_by_nonzero(self):
        result = MathOperations().divide(10.0, 2.0)
        self.assertAlmostEqual(result, 5.0)
    def test_division_error_on_zero(self):
        with self.assertRaises(ValueError):
            MathOperations().divide(10.0, 0.0)
if __name__ == '__main__':
    unittest.main()