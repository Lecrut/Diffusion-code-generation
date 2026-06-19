import unittest

def numbers_differ(num1, num2):
    return num1 != num2

class TestNumbersDiffer(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(numbers_differ(5, 3))
        self.assertFalse(numbers_differ(4, 4))

    def test_negative_numbers(self):
        self.assertTrue(numbers_differ(-1, -3))
        self.assertFalse(numbers_differ(-2, -2))

    def test_zero(self):
        self.assertTrue(numbers_differ(0, -1))
        self.assertFalse(numbers_differ(0, 0))

    def test_floating_point_numbers(self):
        self.assertTrue(numbers_differ(1.5, 1.4))
        self.assertFalse(numbers_differ(2.3, 2.3))
if __name__ == '__main__':
    print(numbers_differ(5, 3))
    print(numbers_differ(-1, -1))
    print(numbers_differ(0, 0))
    print(numbers_differ(1.2, 1.3))
    unittest.main(argv=[''], exit=False)