import unittest
def check_equality(a, b):
    if type(a) is type(b):
        return a == b
    return False
class TestCheckEquality(unittest.TestCase):
    def test_integer_equality(self):
        self.assertTrue(check_equality(5, 5))
        self.assertFalse(check_equality(5, 6))
        self.assertFalse(check_equality(5, 4))
    def test_float_equality(self):
        self.assertTrue(check_equality(3.14, 3.14))
        self.assertFalse(check_equality(3.14, 3.15))
        self.assertFalse(check_equality(3.14, 3.13))
    def test_string_equality(self):
        self.assertTrue(check_equality("hello", "hello"))
        self.assertFalse(check_equality("hello", "world"))
        self.assertFalse(check_equality("hello", "hello "))
    def test_mixed_type_inequality(self):
        self.assertFalse(check_equality(5, 5.0))
        self.assertFalse(check_equality(5, "5"))
        self.assertFalse(check_equality(5.0, 5))
        self.assertFalse(check_equality("a", 1))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)