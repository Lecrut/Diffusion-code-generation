from math import pi

class EllipseMetrics:
    def __init__(self, axis_a, axis_b):
        if axis_a <= 0 or axis_b <= 0:
            raise ValueError("Axes must be positive numbers")
        self.axis_a = float(axis_a)
        self.axis_b = float(axis_b)

    def compute_area(self):
        return pi * self.axis_a * self.axis_b

if __name__ == '__main__':
    try:
        ellipse = EllipseMetrics(5.0, 3.0)
        area_result = ellipse.compute_area()
        print(area_result)
    except ValueError as e:
        print(f"Error: {e}")