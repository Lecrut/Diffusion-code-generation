import unittest

def get_opposite(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")
    return not value

class TestBooleanFlipper(unittest.TestCase):
    def test_get_opposite_true(self):
        self.assertFalse(get_opposite(True))

    def test_get_opposite_false(self):
        self.assertTrue(get_opposite(False))

if __name__ == '__main__':
    unittest.main()