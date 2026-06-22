import math

class Square:
    def __init__(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area
        self.side_length = math.sqrt(area)

    def calculate_perimeter(self):
        return 4 * self.side_length

def compute_square_properties(area):
    try:
        square = Square(area)
        side_length = square.side_length
        perimeter = square.calculate_perimeter()
        return side_length, perimeter
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    area = 16
    side_length, perimeter = compute_square_properties(area)
    print(f"Side Length: {side_length}, Perimeter: {perimeter}")