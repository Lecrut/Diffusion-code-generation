import unittest
class TestAtLeastOneTrue(unittest.TestCase):
    def check_at_least_one_true(self, list_of_booleans):
        return any(list_of_booleans)
    def test_empty_list(self):
        self.assertFalse(self.check_at_least_one_true([]))
    def test_all_false(self):
        self.assertFalse(self.check_at_least_one_true([False, False, False]))
    def test_all_true(self):
        self.assertTrue(self.check_at_least_one_true([True, True, True]))
    def test_mixed_values_one_true(self):
        self.assertTrue(self.check_at_least_one_true([False, False, True, False]))
    def test_mixed_values_one_true_at_end(self):
        self.assertTrue(self.check_at_least_one_true([False, False, False, True]))
    def test_mixed_values_all_false(self):
        self.assertFalse(self.check_at_least_one_true([False, False, False, False]))
    def test_single_true(self):
        self.assertTrue(self.check_at_least_one_true([True]))
    def test_single_false(self):
        self.assertFalse(self.check_at_least_one_true([False]))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)