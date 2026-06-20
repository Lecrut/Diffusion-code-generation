import unittest

class AtLeastOneChecker:
    def check_at_least_one(self, list_of_booleans):
        return any(list_of_booleans)

class TestAtLeastOne(unittest.TestCase):
    def setUp(self):
        self.checker = AtLeastOneChecker()

    def test_empty_list(self):
        self.assertFalse(self.checker.check_at_least_one([]))

    def test_all_false(self):
        self.assertFalse(self.checker.check_at_least_one([False, False, False]))

    def test_mixed_true(self):
        self.assertTrue(self.checker.check_at_least_one([False, True, False]))

    def test_single_true(self):
        self.assertTrue(self.checker.check_at_least_one([True]))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)