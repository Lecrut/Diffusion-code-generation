import unittest

def sum_two_numbers(a, b):
    return a + b

class TestSumTwoNumbers(unittest.TestCase):
    def test_sum_positive_numbers(self):
        self.assertEqual(sum_two_numbers(3, 5), 8)

    def test_sum_negative_numbers(self):
        self.assertEqual(sum_two_numbers(-1, -2), -3)

    def test_sum_mixed_numbers(self):
        self.assertEqual(sum_two_numbers(-1, 2), 1)

    def test_sum_zero(self):
        self.assertEqual(sum_two_numbers(0, 0), 0)

if __name__ == '__main__':
    result = sum_two_numbers(7, 3)
    print(result)
    unittest.main(argv=[''], exit=False)