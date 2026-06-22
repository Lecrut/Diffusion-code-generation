class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

def main():
    try:
        rect = Rectangle(10.0, 4.5)
        print(rect.perimeter())
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()