import unittest
class TestAtLeastOne(unittest.TestCase):
    def check_at_least_one(self, list_of_bools):
        return any(list_of_bools)
    def test_empty_list(self):
        self.assertFalse(self.check_at_least_one([]))
    def test_all_false(self):
        self.assertFalse(self.check_at_least_one([False, False, False]))
    def test_some_true(self):
        self.assertTrue(self.check_at_least_one([False, False, True]))
    def test_all_true(self):
        self.assertTrue(self.check_at_least_one([True, True, True]))
    def test_mixed_values(self):
        self.assertTrue(self.check_at_least_one([False, True, False, True]))
    def test_single_true(self):
        self.assertTrue(self.check_at_least_one([False, False, True]))
    def test_single_false(self):
        self.assertFalse(self.check_at_least_one([False, False, False]))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)