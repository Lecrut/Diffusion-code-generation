import unittest
def calculate_circle_area(radius):
    return 3.14159 * radius * radius
class TestCircleArea(unittest.TestCase):
    def test_positive_radii(self):
        self.assertAlmostEqual(calculate_circle_area(1), 3.14159)
        self.assertAlmostEqual(calculate_circle_area(2), 12.56636)
        self.assertAlmostEqual(calculate_circle_area(0.5), 0.7853975)
        self.assertAlmostEqual(calculate_circle_area(10), 314.159)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)