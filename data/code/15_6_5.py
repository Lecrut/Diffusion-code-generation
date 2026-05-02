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
        self.assertFalse(check_equality(1.0, 1.0000000000000001))
    def test_string_equality(self):
        self.assertTrue(check_equality("hello", "hello"))
        self.assertFalse(check_equality("hello", "world"))
        self.assertTrue(check_equality("", ""))
        self.assertFalse(check_equality("a", "b"))
    def test_mixed_types_equality(self):
        self.assertTrue(check_equality(10, 10.0))
        self.assertFalse(check_equality(10, "10"))
        self.assertFalse(check_equality(5.0, 5))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)