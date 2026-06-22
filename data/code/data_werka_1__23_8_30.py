import unittest

def compare_numbers(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

class TestCompareNumbers(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(compare_numbers(5, 3), 1)
        self.assertEqual(compare_numbers(3, 5), -1)

    def test_negative_numbers(self):
        self.assertEqual(compare_numbers(-5, -3), -1)
        self.assertEqual(compare_numbers(-3, -5), 1)

    def test_mixed_signs(self):
        self.assertEqual(compare_numbers(-5, 3), -1)
        self.assertEqual(compare_numbers(5, -3), 1)

    def test_zero_cases(self):
        self.assertEqual(compare_numbers(0, 0), 0)
        self.assertEqual(compare_numbers(0, 5), -1)
        self.assertEqual(compare_numbers(5, 0), 1)

    def test_small_differences(self):
        self.assertEqual(compare_numbers(0.1 + 0.2, 0.3), 0)
        self.assertEqual(compare_numbers(0.1 - 0.2, -0.1), 0)

    def test_large_numbers(self):
        self.assertEqual(compare_numbers(10000000000.0, 1000000000.0), 1)
        self.assertEqual(compare_numbers(1000000000.0, 10000000000.0), -1)
if __name__ == '__main__':
    print(compare_numbers(5, 3))
    print(compare_numbers(-5, -3))
    print(compare_numbers(0, 0))
    print(compare_numbers(0.1 + 0.2, 0.3))
    unittest.main(argv=[''], exit=False)