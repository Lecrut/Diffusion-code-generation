import unittest

def opposite_truth(value: bool) -> bool:
    return not value

class TestOppositeTruth(unittest.TestCase):
    def test_opposite_of_true(self):
        self.assertFalse(opposite_truth(True))
    
    def test_opposite_of_false(self):
        self.assertTrue(opposite_truth(False))

if __name__ == '__main__':
    sample_values = [True, False]
    for value in sample_values:
        print(f"Input: {value}, Output: {opposite_truth(value)}")