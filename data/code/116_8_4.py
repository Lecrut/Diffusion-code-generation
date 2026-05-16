import unittest
def sum_three(a, b, c):
    return a + b + c
class TestSumThree(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_three(1, 2, 3), 6)
    def test_with_negative_numbers(self):
        self.assertEqual(sum_three(-1, 5, -3), 1)
    def test_with_zero(self):
        self.assertEqual(sum_three(0, 0, 0), 0)
    def test_with_mixed_numbers(self):
        self.assertEqual(sum_three(10, -5, 2), 7)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)