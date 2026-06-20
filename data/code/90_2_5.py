import unittest

class OrCondition:
    def evaluate_or(self, a, b):
        return a or b

class TestOrCondition(unittest.TestCase):
    def test_true_or_true(self):
        self.assertTrue(True or True)
    
    def test_true_or_false(self):
        self.assertTrue(True or False)
    
    def test_false_or_true(self):
        self.assertTrue(False or True)
    
    def test_false_or_false(self):
        self.assertFalse(False or False)
    
    def test_or_with_integers(self):
        result = OrCondition().evaluate_or(0, 1)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)