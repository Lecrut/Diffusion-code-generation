import math

def calculate_square_area(side_length):
    return side_length ** 2

if __name__ == '__main__':
    side = 5.0
    area = calculate_square_area(side)
    print(f"The area of a square with side {side} is {area}")