import unittest

def is_larger_than(a: int, b: int) -> bool:
    """Returns True if a > b (strictly larger), False otherwise."""
    return a > b

class TestIsLarger(unittest.TestCase):
    def test_positive_inequality(self):
        self.assertTrue(is_larger_than(5, 3))

    def test_negative_inequality(self):
        self.assertFalse(is_larger_than(-2, -5))

    def test_equality_case(self):
        self.assertFalse(is_larger_than(10, 10))

    def test_zero_and_positive(self):
        self.assertTrue(is_larger_than(0, -1))

    def test_negative_vs_zero(self):
        self.assertFalse(is_larger_than(-5, 0))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIsLarger)
    runner = unittest.TextTestRunner()
    runner.run(suite)