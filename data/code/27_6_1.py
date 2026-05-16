import unittest
def do_numbers_differ(a, b):
    return a != b
class TestNumberDifference(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(do_numbers_differ(5, 10))
        self.assertFalse(do_numbers_differ(5, 5))
    def test_negative_numbers(self):
        self.assertTrue(do_numbers_differ(-5, -10))
        self.assertFalse(do_numbers_differ(-5, -5))
        self.assertTrue(do_numbers_differ(-10, -5))
    def test_mixed_signs(self):
        self.assertTrue(do_numbers_differ(5, -5))
        self.assertFalse(do_numbers_differ(5, 5))
        self.assertTrue(do_numbers_differ(-5, 5))
    def test_involving_zero(self):
        self.assertTrue(do_numbers_differ(0, 5))
        self.assertFalse(do_numbers_differ(0, 0))
        self.assertTrue(do_numbers_differ(-5, 0))
        self.assertTrue(do_numbers_differ(0, -5))
    def test_floating_point_numbers(self):
        self.assertTrue(do_numbers_differ(1.1, 1.2))
        self.assertFalse(do_numbers_differ(3.14, 3.14))
        self.assertTrue(do_numbers_differ(0.0, 0.001))
        self.assertFalse(do_numbers_differ(1.0, 1.0))
        self.assertTrue(do_numbers_differ(-1.5, -1.50001))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)