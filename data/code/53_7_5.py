import unittest
class TestSquareArea(unittest.TestCase):
    def test_calculate_area(self):
        self.assertEqual(calculate_square_area(5), 25)
        self.assertEqual(calculate_square_area(10), 100)
        self.assertEqual(calculate_square_area(0), 0)
        self.assertEqual(calculate_square_area(3.5), 12.25)
def calculate_square_area(side):
    return side * side
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)