import unittest

def calculate_circle_area(radius):
    import math
    return math.pi * radius ** 2

class TestCircleArea(unittest.TestCase):
    def test_positive_radius(self):
        self.assertAlmostEqual(calculate_circle_area(1), 3.141592653589793)
        self.assertAlmostEqual(calculate_circle_area(0.5), 0.7853981633974483)
        self.assertAlmostEqual(calculate_circle_area(2.5), 19.634954084936208)

if __name__ == '__main__':
    print(calculate_circle_area(1))
    unittest.main(argv=[''], exit=False)