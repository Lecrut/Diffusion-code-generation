import math

class Square:
    SQUARE_ROOT_OF_TWO = 2 ** 0.5
    
    @staticmethod
    def compute_side_length(area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        return area ** Square.SQUARE_ROOT_OF_TWO
    
    @staticmethod
    def compute_perimeter(side_length):
        return 4 * side_length

if __name__ == '__main__':
    square_area = 16
    try:
        side_length = Square.compute_side_length(square_area)
        perimeter = Square.compute_perimeter(side_length)
        print(f"Side Length: {side_length}, Perimeter: {perimeter}")
    except ValueError as e:
        print(e)