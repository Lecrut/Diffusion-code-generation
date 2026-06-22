class Circle:
    def __init__(self, radius: float):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be an integer or float.")
        self.radius = radius

    def calculate_area(self) -> float:
        return 3.141592653589793 * self.radius ** 2

if __name__ == '__main__':
    circle_instance = Circle(5.0)
    area_of_circle = circle_instance.calculate_area()
    print(f"Area of the circle with radius 5.0: {area_of_circle}")
    
    another_circle = Circle(10.0)
    another_area = another_circle.calculate_area()
    print(f"Area of another circle with radius 10.0: {another_area}")