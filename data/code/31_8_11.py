import math

def calculate_square_area(side_length):
    return math.pow(side_length, 2)

if __name__ == '__main__':
    side = 4.5
    area = calculate_square_area(side)
    print(area)