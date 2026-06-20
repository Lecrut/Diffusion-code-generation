import unittest

class TestAtLeastOne(unittest.TestCase):
    def check_at_least_one(self, list_of_booleans):
        return any(list_of_booleans)

    def test_empty_list(self):
        self.assertFalse(self.check_at_least_one([]))

    def test_all_false(self):
        self.assertFalse(self.check_at_least_one([False] * 5))

    def test_mixed_values(self):
        self.assertTrue(self.check_at_least_one([True, False, True]))

    def test_single_true(self):
        self.assertTrue(self.check_at_least_one([True]))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)