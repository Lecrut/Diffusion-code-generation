class Shape:
    def __init__(self, length: float, width: float):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.length = length
        self.width = width

    def calculate_perimeter(self) -> float:
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    try:
        shape_instance = Shape(8.0, 6.0)
        perimeter = shape_instance.calculate_perimeter()
        print(perimeter)
    except ValueError as e:
        print(e)