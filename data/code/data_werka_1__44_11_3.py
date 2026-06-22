class Rectangle:
    def __init__(self, length: float, width: float):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.length = length
        self.width = width

    def calculate_perimeter(self) -> float:
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    try:
        rect = Rectangle(10.5, 5.0)
        perimeter = rect.calculate_perimeter()
        print(perimeter)
    except ValueError as e:
        print(e)