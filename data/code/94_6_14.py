import unittest

def at_least_one_true(input_list):
    if not isinstance(input_list, list) or not all(isinstance(item, bool) for item in input_list):
        raise ValueError("Input must be a list of booleans")
    return any(input_list)

class TestAtLeastOneTrue(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(at_least_one_true([]))

    def test_all_false(self):
        self.assertFalse(at_least_one_true([False, False, False]))

    def test_single_true(self):
        self.assertTrue(at_least_one_true([True]))

    def test_mixed_values(self):
        self.assertTrue(at_least_one_true([False, True, False]))

    def test_single_false(self):
        self.assertFalse(at_least_one_true([False]))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)