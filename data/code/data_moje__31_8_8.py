import math
POWER_EXPONENT = 2.0

def calculate_square_area(side_length):
    return float(math.pow(side_length, POWER_EXPONENT))

if __name__ == '__main__':
    TEST_SIDE_LENGTH = 7.25
    computed_area = calculate_square_area(TEST_SIDE_LENGTH)
    print(computed_area)