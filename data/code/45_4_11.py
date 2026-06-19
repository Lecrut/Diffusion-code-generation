import math

class Circle:

    def __init__(self, diameter):
        if diameter <= 0:
            raise ValueError('Diameter must be a positive number.')
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_area(self):
        return math.pi * self.radius ** 2

def test_circle_area():
    circle1 = Circle(10)
    assert abs(circle1.calculate_area() - math.pi * 25) < 1e-09, 'Test case for diameter 10 failed'
    try:
        Circle(0)
    except ValueError as e:
        assert str(e) == 'Diameter must be a positive number.', 'Test case for diameter 0 failed'
    try:
        Circle(-5)
    except ValueError as e:
        assert str(e) == 'Diameter must be a positive number.', 'Test case for diameter -5 failed'
if __name__ == '__main__':
    test_circle_area()
    print('All tests passed.')
    circle = Circle(10)
    print(f'The area of a circle with diameter {circle.diameter} is: {circle.calculate_area()}')