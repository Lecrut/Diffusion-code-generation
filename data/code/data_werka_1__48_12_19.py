import math

class Square:
    def __init__(self, area):
        if area <= 0:
            raise ValueError("Area must be positive")
        self.area = area
        self.side_length = math.sqrt(area)

    def calculate_perimeter(self):
        return 4 * self.side_length

def main():
    try:
        square = Square(16)
        print(f"Side Length: {square.side_length}")
        print(f"Perimeter: {square.calculate_perimeter()}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()