import unittest

def check_both_false(a, b):
    return not a and not b

class TestCheckBothFalse(unittest.TestCase):
    def test_cases(self):
        cases = [
            (False, False, True),
            (True, False, False),
            (False, True, False),
            (True, True, False),
            (0, 0, True),
            (1, 1, False)
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                result = check_both_false(a, b)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)