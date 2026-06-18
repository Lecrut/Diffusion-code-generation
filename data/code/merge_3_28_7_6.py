import unittest

def is_greater(value_a: float, value_b: float) -> bool:
    """Determines if value_a is strictly larger than value_b."""
    return value_a > value_b

class TestIsGreater(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(is_greater(10.5, 3))

    def test_negative_numbers(self):
        self.assertFalse(is_greater(-5, -2))
        self.assertEqual(is_greater(-10, -9), False)

    def test_equal_values(self):
        result = is_greater(7, 7)
        self.assertIsInstance(result, bool)
        self.assertFalse(result)

    def test_zero_vs_positive(self):
        self.assertTrue(is_greater(5.0, 0))

    def test_negative_vs_zero(self):
        # -1 should not be greater than 0
        result = is_greater(-1.0, 0)
        self.assertIsInstance(result, bool)
        self.assertFalse(result)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIsGreater)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Run a quick manual check with hard-coded sample values as requested in the block description context
    samples_to_check = [
        (10, 5),      # True
        (-3, -1),     # False: -3 is not greater than -1
        (4.2, 4.2),   # False: equality returns False
        (-99, 876)    # True
    ]

    print("\n--- Manual Sample Checks ---")
    for a, b in samples_to_check:
        outcome = is_greater(a, b)
        expected = a > b
        status = "PASS" if outcome == expected else "FAIL"
        print(f"is_greater({a}, {b}) = {outcome} (Expected: {expected}) -> [{status}]")

    # Exit with error code if any manual check failed or unit tests failed
    if not result.wasSuccessful():
        exit(1)