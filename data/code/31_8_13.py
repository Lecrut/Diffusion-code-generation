import math

SIDE_EXPONENT = 2

def compute_area(side_length):
    return float(math.pow(side_length, SIDE_EXPONENT))

if __name__ == '__main__':
    side_value = 4.2
    area_value = compute_area(side_value)
    print(area_value)