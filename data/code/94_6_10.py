import unittest

def check_at_least_one(list_of_booleans):
    if not all(isinstance(x, bool) for x in list_of_booleans):
        raise ValueError("All elements in the list must be boolean values.")
    return any(list_of_booleans)

class TestAtLeastOne(unittest.TestCase):
    def test_mixed_true(self):
        self.assertTrue(check_at_least_one([False, True, False]))
    
    def test_all_false(self):
        self.assertFalse(check_at_least_one([False, False, False]))
    
    def test_all_true(self):
        self.assertTrue(check_at_least_one([True, True, True]))
    
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            check_at_least_one([])
    
    def test_single_true(self):
        self.assertTrue(check_at_least_one([True]))
    
    def test_single_false(self):
        self.assertFalse(check_at_least_one([False]))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)