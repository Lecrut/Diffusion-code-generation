class Square:
    def __init__(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area

    def calculate_side_length(self):
        return self.area ** 0.5

    def get_area(self):
        return self.area

if __name__ == '__main__':
    EXAMPLE_AREA = 25.0
    square = Square(EXAMPLE_AREA)
    side_length = square.calculate_side_length()
    area = square.get_area()
    
    print(f"Side Length: {side_length}")
    print(f"Area: {area}")