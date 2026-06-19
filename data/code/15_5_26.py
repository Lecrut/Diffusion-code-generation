import unittest

def check_equality(a, b):
    return a == b

class TestCheckEquality(unittest.TestCase):

    def test_integers(self):
        self.assertTrue(check_equality(10, 10))
        self.assertFalse(check_equality(10, 20))

    def test_floats(self):
        self.assertTrue(check_equality(10.5, 10.5))
        self.assertFalse(check_equality(10.5, 20.3))

    def test_strings(self):
        self.assertTrue(check_equality('hello', 'hello'))
        self.assertFalse(check_equality('hello', 'world'))
if __name__ == '__main__':
    print(check_equality(10, 10))
    print(check_equality(10.5, 20.3))
    print(check_equality('hello', 'world'))
    unittest.main(argv=[''], exit=False)