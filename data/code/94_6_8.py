import unittest

def at_least_one_true(lst):
    return any(lst)

class TestAtLeastOneTrue(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(at_least_one_true([]))

    def test_all_false(self):
        self.assertFalse(at_least_one_true([False, False, False]))

    def test_mixed_values(self):
        self.assertTrue(at_least_one_true([False, True, False]))
        self.assertTrue(at_least_one_true([True, False, False]))

if __name__ == '__main__':
    unittest.main()