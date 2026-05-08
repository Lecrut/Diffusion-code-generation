import unittest
def check_odd_numbers(numbers):
    return all(x % 2 != 0 for x in numbers)
class TestOddNumberChecker(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(check_odd_numbers([]))
    def test_all_even(self):
        self.assertFalse(check_odd_numbers([2, 4, 6, 8]))
    def test_all_odd(self):
        self.assertTrue(check_odd_numbers([1, 3, 5, 7]))
    def test_mixed_numbers(self):
        self.assertFalse(check_odd_numbers([1, 2, 3, 4]))
    def test_single_odd(self):
        self.assertTrue(check_odd_numbers([5]))
    def test_single_even(self):
        self.assertFalse(check_odd_numbers([6]))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)