def is_odd(n: int) -> bool:
    """Return True if n is odd, False otherwise."""
    return n % 2 == 1

if __name__ == '__main__':
    test_cases = [5, 8]
    for num in test_cases:
        result = is_odd(num)
        print(f"Number {num} is {'odd' if result else 'even'}")

# To run tests explicitly (optional usage):
from unittest import TestCase

class TestIsOdd(TestCase):
    def test_5_is_odd(self):
        self.assertTrue(is_odd(5))

    def test_8_is_even(self):
        self.assertFalse(is_odd(8))