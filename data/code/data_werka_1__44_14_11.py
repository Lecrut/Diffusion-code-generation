class Rectangle:
    def __init__(self, width: int, height: int):
        if not isinstance(width, int) or not isinstance(height, int):
            raise ValueError("Both width and height must be integers.")
        if width <= 0 or height <= 0:
            raise ValueError("Both width and height must be positive integers.")
        self.width = width
        self.height = height

    def perimeter(self) -> int:
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    try:
        rect = Rectangle(5, 3)
        print(rect.perimeter())
    except ValueError as e:
        print(e)