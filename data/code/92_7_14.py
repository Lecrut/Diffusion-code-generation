import unittest

def get_opposite(value: bool) -> bool:
    return not value

class TestBooleanOpposite(unittest.TestCase):
    def test_true_to_false(self):
        self.assertFalse(get_opposite(True))

    def test_false_to_true(self):
        self.assertTrue(get_opposite(False))

if __name__ == '__main__':
    unittest.main()