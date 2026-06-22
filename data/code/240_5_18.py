class Square:
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

if __name__ == '__main__':
    square_instance = Square(4)
    area = square_instance.calculate_area()
    print(f"Side: 4, Area: {area}")