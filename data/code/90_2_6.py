import unittest

class TestOrCondition(unittest.TestCase):
    def test_or_true_true(self):
        self.assertTrue(True or True)
    
    def test_or_true_false(self):
        self.assertTrue(True or False)
    
    def test_or_false_true(self):
        self.assertTrue(False or True)
    
    def test_or_false_false(self):
        self.assertFalse(False or False)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)