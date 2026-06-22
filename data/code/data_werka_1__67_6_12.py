import unittest

def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")

def sum_two_numbers(a, b):
    validate_numbers(a, b)
    return a + b

class TestSumTwoNumbers(unittest.TestCase):
    def test_sum_positive_numbers(self):
        self.assertEqual(sum_two_numbers(3, 4), 7)

    def test_sum_negative_numbers(self):
        self.assertEqual(sum_two_numbers(-1, -2), -3)

    def test_sum_mixed_numbers(self):
        self.assertEqual(sum_two_numbers(-1, 2), 1)

    def test_sum_zero(self):
        self.assertEqual(sum_two_numbers(0, 0), 0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            sum_two_numbers('a', 2)

if __name__ == '__main__':
    sample_a = 15
    sample_b = 25
    result = sum_two_numbers(sample_a, sample_b)
    print(result)
    unittest.main(argv=[''], exit=False)