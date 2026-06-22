import operator
import math

CONST_BASE = 7
CONST_HEIGHT = 4

def calculate_area(base, height):
    return operator.mul(base, height)

if __name__ == '__main__':
    area_result = calculate_area(CONST_BASE, CONST_HEIGHT)
    print(area_result)