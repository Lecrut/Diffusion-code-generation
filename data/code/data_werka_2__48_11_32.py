import math

class SquareCalculator:
    SQRT_TWO = math.sqrt(2)
    
    @staticmethod
    def compute_side_length(area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        return math.sqrt(area)
    
    @staticmethod
    def compute_perimeter(side_length):
        return 4 * side_length

if __name__ == '__main__':
    square_area = 16
    try:
        side_length = SquareCalculator.compute_side_length(square_area)
        perimeter = SquareCalculator.compute_perimeter(side_length)
        print(f"Side Length: {side_length}, Perimeter: {perimeter}")
    except ValueError as e:
        print(e)