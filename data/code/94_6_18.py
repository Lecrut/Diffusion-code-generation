import unittest

class AtLeastOneChecker:
    def check_condition(self, list_of_booleans):
        return any(list_of_booleans)

class TestAtLeastOne(unittest.TestCase):
    def test_empty_list(self):
        checker = AtLeastOneChecker()
        self.assertFalse(checker.check_condition([]))

    def test_all_false(self):
        checker = AtLeastOneChecker()
        self.assertFalse(checker.check_condition([False, False, False]))

    def test_mixed_true(self):
        checker = AtLeastOneChecker()
        self.assertTrue(checker.check_condition([False, True, False]))

    def test_single_true(self):
        checker = AtLeastOneChecker()
        self.assertTrue(checker.check_condition([True]))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)