import unittest

def get_opposite(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return not value

class TestBooleanFlipper(unittest.TestCase):
    def test_true(self):
        self.assertFalse(get_opposite(True))

    def test_false(self):
        self.assertTrue(get_opposite(False))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            get_opposite("not a boolean")

if __name__ == '__main__':
    unittest.main()