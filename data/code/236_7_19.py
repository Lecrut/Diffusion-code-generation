class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be greater than zero.")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

@staticmethod
def create_five_rectangles():
    return [Rectangle(10, 5) for _ in range(5)]

if __name__ == '__main__':
    rectangles = create_five_rectangles()
    for rect in rectangles:
        print(f"Rectangle width: {rect.width}, height: {rect.height}, area: {rect.area()}")