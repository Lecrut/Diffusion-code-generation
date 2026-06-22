import math

def calculate_square_area(side):
    return float(math.pow(side, 2))

if __name__ == '__main__':
    side_length = 5.5
    area = calculate_square_area(side_length)
    print(area)