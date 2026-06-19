import unittest

def numbers_differ(a, b):
    return a != b

class TestNumbersDiffer(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(numbers_differ(5, 10))
        self.assertFalse(numbers_differ(7, 7))

    def test_negative_numbers(self):
        self.assertTrue(numbers_differ(-3, -8))
        self.assertFalse(numbers_differ(-2, -2))

    def test_zero(self):
        self.assertTrue(numbers_differ(0, 5))
        self.assertFalse(numbers_differ(0, 0))

    def test_floating_point_numbers(self):
        self.assertTrue(numbers_differ(1.5, 2.5))
        self.assertFalse(numbers_differ(3.0, 3.0))
        self.assertTrue(numbers_differ(0.1 + 0.2, 0.3))
if __name__ == '__main__':
    print(numbers_differ(5, 10))
    print(numbers_differ(-7, -7))
    print(numbers_differ(0, 0))
    print(numbers_differ(0.1 + 0.2, 0.3))
    unittest.main(argv=[''], exit=False)