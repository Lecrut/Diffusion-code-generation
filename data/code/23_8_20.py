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
        self.assertEqual(compare_numbers(5, 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(compare_numbers(-5, -3), -1)
        self.assertEqual(compare_numbers(-3, -5), 1)
        self.assertEqual(compare_numbers(-5, -5), 0)

    def test_mixed_signs(self):
        self.assertEqual(compare_numbers(5, -3), 1)
        self.assertEqual(compare_numbers(-3, 5), -1)
        self.assertEqual(compare_numbers(0, -1), 1)
        self.assertEqual(compare_numbers(-1, 0), -1)

    def test_zero(self):
        self.assertEqual(compare_numbers(0, 0), 0)
        self.assertEqual(compare_numbers(0, 1), -1)
        self.assertEqual(compare_numbers(1, 0), 1)

    def test_very_small_differences(self):
        self.assertEqual(compare_numbers(1e-07, 2e-07), -1)
        self.assertEqual(compare_numbers(2e-07, 1e-07), 1)
        self.assertEqual(compare_numbers(1e-07, 1e-07), 0)
if __name__ == '__main__':
    print(compare_numbers(5, 3))
    print(compare_numbers(-5, -3))
    print(compare_numbers(0, 0))
    print(compare_numbers(1e-07, 2e-07))
    unittest.main(argv=[''], exit=False)