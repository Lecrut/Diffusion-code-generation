import unittest
def calculate_circle_area(radius):
    return 3.141592653589793 * radius * radius
class TestCircleArea(unittest.TestCase):
    def test_positive_radii(self):
        self.assertAlmostEqual(calculate_circle_area(1), 3.141592653589793)
        self.assertAlmostEqual(calculate_circle_area(2), 12.566370614359172)
        self.assertAlmostEqual(calculate_circle_area(0.5), 0.7853981633974483)
        self.assertAlmostEqual(calculate_circle_area(10), 314.1592653589793)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)