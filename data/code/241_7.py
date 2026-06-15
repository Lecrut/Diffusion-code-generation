import unittest
def calculate_area(length, width):
    return length * width
class TestAreaCalculator(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(calculate_area(5, 10), 50)
        self.assertEqual(calculate_area(2, 3), 6)
        self.assertEqual(calculate_area(1, 1), 1)
        self.assertEqual(calculate_area(100, 5), 500)
        self.assertEqual(calculate_area(7, 7), 49)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)