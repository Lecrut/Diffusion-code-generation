import unittest

class TestOrCondition(unittest.TestCase):
    def test_true_or_true(self):
        self.assertTrue(True or True)

    def test_true_or_false(self):
        self.assertTrue(True or False)
        self.assertTrue(False or True)

    def test_false_or_true(self):
        self.assertTrue(False or True)
        self.assertTrue(True or False)

    def test_false_or_false(self):
        self.assertFalse(False or False)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestOrCondition('test_true_or_true'))
    suite.addTest(TestOrCondition('test_true_or_false'))
    suite.addTest(TestOrCondition('test_false_or_true'))
    suite.addTest(TestOrCondition('test_false_or_false'))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("Total tests run:", result.testsRun)
    print("Tests passed:", result.testsRun - len(result.failures))
    print("Tests failed:", len(result.failures))