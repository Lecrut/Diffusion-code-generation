def validate_radius(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive")
    return radius
class CircleArea:
    def __init__(self, radius):
        self.radius = validate_radius(radius)
    def calculate_area(self):
        return 3.14159 * self.radius ** 2
if __name__ == '__main__':
    try:
        area1 = CircleArea(5)
        print(f"Area 1: {area1.calculate_area()}")
        area2 = CircleArea(10.5)
        print(f"Area 2: {area2.calculate_area()}")
        try:
            area3 = CircleArea(-2)
        except ValueError as e:
            print(f"Error for radius -2: {e}")
        try:
            area4 = CircleArea(0)
        except ValueError as e:
            print(f"Error for radius 0: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")