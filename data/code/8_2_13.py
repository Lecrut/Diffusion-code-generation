class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    PI = 3.141592653589793

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calculate_area(self) -> float:
        return Shape.PI * (self.radius ** 2)

if __name__ == '__main__':
    rect = Rectangle(5.0, 10.0)
    circle = Circle(3.0)

    print(f"Rectangle Area: {rect.calculate_area()}")
    print(f"Circle Area: {circle.calculate_area()}")