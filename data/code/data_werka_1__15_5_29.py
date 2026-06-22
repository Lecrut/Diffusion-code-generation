import unittest

def check_equality(a, b):
    return a == b

class TestCheckEquality(unittest.TestCase):

    def test_integers(self):
        self.assertTrue(check_equality(1, 1))
        self.assertFalse(check_equality(1, 2))

    def test_floats(self):
        self.assertTrue(check_equality(1.0, 1.0))
        self.assertFalse(check_equality(1.0, 1.1))

    def test_strings(self):
        self.assertTrue(check_equality('hello', 'hello'))
        self.assertFalse(check_equality('hello', 'world'))
if __name__ == '__main__':
    print(check_equality(5, 5))
    print(check_equality(3.14, 3.14))
    print(check_equality('test', 'test'))
    unittest.main(argv=[''], exit=False)