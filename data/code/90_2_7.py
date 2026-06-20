import unittest

class OrConditionTest(unittest.TestCase):
    OR_TRUE = True
    OR_FALSE = False
    
    def test_or_true_true(self):
        self.assertTrue(OrConditionTest.OR_TRUE or OrConditionTest.OR_TRUE)
    
    def test_or_true_false(self):
        self.assertTrue(OrConditionTest.OR_TRUE or OrConditionTest.OR_FALSE)
    
    def test_or_false_true(self):
        self.assertTrue(OrConditionTest.OR_FALSE or OrConditionTest.OR_TRUE)
    
    def test_or_false_false(self):
        self.assertFalse(OrConditionTest.OR_FALSE or OrConditionTest.OR_FALSE)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)