import unittest

class BooleanFlipper:
    @staticmethod
    def get_opposite(state: bool) -> bool:
        return not state

class TestBooleanFlipper(unittest.TestCase):
    def test_get_opposite(self):
        self.assertFalse(BooleanFlipper.get_opposite(True))
        self.assertTrue(BooleanFlipper.get_opposite(False))

if __name__ == '__main__':
    unittest.main()