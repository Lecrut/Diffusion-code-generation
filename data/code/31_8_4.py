import math

def square_area(side):
    return math.pow(side, 2)

if __name__ == '__main__':
    side_length = 5.0
    area = square_area(side_length)
    print(area)