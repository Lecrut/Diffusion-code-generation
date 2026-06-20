import unittest

class OrConditionTester:
    def test_or_true_true(self):
        return True or True
    
    def test_or_true_false(self):
        return True or False
    
    def test_or_false_true(self):
        return False or True
    
    def test_or_false_false(self):
        return False or False

if __name__ == '__main__':
    tester = OrConditionTester()
    print(tester.test_or_true_true())
    print(tester.test_or_true_false())
    print(tester.test_or_false_true())
    print(tester.test_or_false_false())