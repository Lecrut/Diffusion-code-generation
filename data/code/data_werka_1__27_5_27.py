import unittest

def numbers_differ(num1, num2):
    return num1 != num2

class TestNumbersDiffer(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(numbers_differ(5, 3))
        self.assertFalse(numbers_differ(7, 7))

    def test_negative_numbers(self):
        self.assertTrue(numbers_differ(-2, -4))
        self.assertFalse(numbers_differ(-8, -8))

    def test_zero(self):
        self.assertTrue(numbers_differ(0, -1))
        self.assertFalse(numbers_differ(0, 0))

    def test_floating_point_numbers(self):
        self.assertTrue(numbers_differ(3.5, 2.5))
        self.assertFalse(numbers_differ(4.0, 4.0))
if __name__ == '__main__':
    print(numbers_differ(10, 5))
    unittest.main(argv=[''], exit=False)