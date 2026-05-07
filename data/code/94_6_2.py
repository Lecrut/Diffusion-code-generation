import unittest
class TestAtLeastOne(unittest.TestCase):
    def check_at_least_one(self, list_of_booleans):
        return any(list_of_booleans)
    def test_empty_list(self):
        self.assertFalse(self.check_at_least_one([]))
    def test_all_false(self):
        self.assertFalse(self.check_at_least_one([False, False, False]))
    def test_mixed_true(self):
        self.assertTrue(self.check_at_least_one([False, False, True]))
    def test_mixed_false(self):
        self.assertFalse(self.check_at_least_one([False, False, False]))
    def test_single_true(self):
        self.assertTrue(self.check_at_least_one([True]))
    def test_single_false(self):
        self.assertFalse(self.check_at_least_one([False]))
    def test_all_true(self):
        self.assertTrue(self.check_at_least_one([True, True, True]))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)