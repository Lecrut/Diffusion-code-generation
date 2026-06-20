import unittest

def at_least_one_is_true(lst):
    return any(lst)

class TestAtLeastOneIsTrue(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(at_least_one_is_true([]))

    def test_all_false_values(self):
        self.assertFalse(at_least_one_is_true([False, False, False]))

    def test_mixed_values(self):
        self.assertTrue(at_least_one_is_true([False, True, False]))
        self.assertTrue(at_least_one_is_true([True, False, False]))
        self.assertTrue(at_least_one_is_true([False, False, True]))

if __name__ == '__main__':
    unittest.main()