import unittest

def check_equality(a, b):
    return a == b

class TestEqualityCheck(unittest.TestCase):

    def test_integers(self):
        self.assertTrue(check_equality(10, 10))
        self.assertFalse(check_equality(5, 10))

    def test_floats(self):
        self.assertTrue(check_equality(3.14, 3.14))
        self.assertFalse(check_equality(2.718, 3.14))

    def test_strings(self):
        self.assertTrue(check_equality('hello', 'hello'))
        self.assertFalse(check_equality('world', 'hello'))
if __name__ == '__main__':
    print(check_equality(5, 5))
    print(check_equality(3.14, 2.718))
    print(check_equality('test', 'test'))
    unittest.main(argv=[''], exit=False)