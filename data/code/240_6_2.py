import math
def calculate_square_area(side):
    area = side * side
    return area
if __name__ == '__main__':
    side_length = 5.0
    area_result = calculate_square_area(side_length)
    print(f"The side length of the square is: {side_length}")
    print(f"The area of the square is: {area_result}")