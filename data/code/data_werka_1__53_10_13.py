import math

class Square:
    DEFAULT_AREA = 25.0
    
    @staticmethod
    def calculate_side_length(area):
        return math.sqrt(area)
    
if __name__ == '__main__':
    side_length = Square.calculate_side_length(Square.DEFAULT_AREA)
    print(f"The side length of the square is: {side_length}")