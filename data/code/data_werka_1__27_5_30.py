import unittest

def numbers_differ(a, b):
    return a != b

class TestNumbersDiffer(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(numbers_differ(5, 3))
        self.assertFalse(numbers_differ(7, 7))

    def test_negative_numbers(self):
        self.assertTrue(numbers_differ(-2, -4))
        self.assertFalse(numbers_differ(-6, -6))

    def test_zero(self):
        self.assertTrue(numbers_differ(0, 1))
        self.assertFalse(numbers_differ(0, 0))

    def test_floating_point_numbers(self):
        self.assertTrue(numbers_differ(3.14, 2.71))
        self.assertFalse(numbers_differ(1.0, 1.0))
if __name__ == '__main__':
    print(numbers_differ(5, 3))
    print(numbers_differ(-6, -6))
    print(numbers_differ(0, 0))
    print(numbers_differ(3.14, 2.71))