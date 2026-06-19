import unittest

def sum_two_numbers(a, b):
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

if __name__ == '__main__':
    sample_a = 7
    sample_b = 8
    result = sum_two_numbers(sample_a, sample_b)
    print(result)
    unittest.main(argv=[''], exit=False)