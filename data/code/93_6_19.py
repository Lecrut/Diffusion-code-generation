import unittest

def check_both_false(a, b):
    return not a and not b

class TestCheckBothFalse(unittest.TestCase):
    def test_cases(self):
        test_data = {
            (False, False): True,
            (True, False): False,
            (False, True): False,
            (True, True): False,
            (1, 0): False,
            (0, 1): False
        }
        
        for inputs, expected in test_data.items():
            with self.subTest(inputs=inputs):
                result = check_both_false(*inputs)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)