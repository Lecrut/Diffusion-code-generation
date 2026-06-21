import math

def square_area(side_length):
    return math.pow(side_length, 2)

if __name__ == '__main__':
    side = 5.0
    area = square_area(side)
    print(area)