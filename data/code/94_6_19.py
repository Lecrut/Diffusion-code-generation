import unittest

def at_least_one_true(list_of_booleans):
    return any(list_of_booleans)

class TestAtLeastOneTrue(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(at_least_one_true([]))
    
    def test_all_false(self):
        self.assertFalse(at_least_one_true([False, False, False]))
    
    def test_mixed_values(self):
        self.assertTrue(at_least_one_true([False, True, False]))
    
    def test_single_true(self):
        self.assertTrue(at_least_one_true([True]))
    
    def test_single_false(self):
        self.assertFalse(at_least_one_true([False]))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)