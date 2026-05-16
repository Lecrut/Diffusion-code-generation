import unittest
def check_equality(a, b):
    return a == b
class TestCheckEquality(unittest.TestCase):
    def test_integer_equality(self):
        self.assertTrue(check_equality(5, 5))
        self.assertFalse(check_equality(5, 6))
        self.assertTrue(check_equality(-1, -1))
        self.assertFalse(check_equality(10, 5))
    def test_float_equality(self):
        self.assertTrue(check_equality(3.14, 3.14))
        self.assertFalse(check_equality(3.14, 3.15))
        self.assertTrue(check_equality(0.0, 0.0))
        self.assertFalse(check_equality(1.0, 2.0))
    def test_string_equality(self):
        self.assertTrue(check_equality("hello", "hello"))
        self.assertFalse(check_equality("hello", "world"))
        self.assertTrue(check_equality("", ""))
        self.assertFalse(check_equality("a", "b"))
    def test_mixed_type_equality(self):
        self.assertFalse(check_equality(5, "5"))
        self.assertFalse(check_equality(3.0, 3))
        self.assertTrue(check_equality(True, 1))
        self.assertFalse(check_equality(True, 0))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)