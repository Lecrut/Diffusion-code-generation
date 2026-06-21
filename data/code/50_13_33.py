class Rectangle:
    def __init__(self, length, width):
        if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
            raise ValueError("Length and width must be numbers.")
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def validate_rectangle(rectangle):
    if not isinstance(rectangle, Rectangle):
        raise ValueError("Both inputs must be instances of Rectangle.")

def find_difference(rect1, rect2):
    validate_rectangle(rect1)
    validate_rectangle(rect2)
    return abs(rect1.area() - rect2.area())

if __name__ == '__main__':
    try:
        length1 = 8
        width1 = 5
        length2 = 6
        width2 = 3

        rect1 = Rectangle(length1, width1)
        rect2 = Rectangle(length2, width2)

        difference = find_difference(rect1, rect2)
        print(f"Difference in areas: {difference}")
    except ValueError as e:
        print(e)