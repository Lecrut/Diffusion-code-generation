import math

SIDE_POWER = 2
VALIDATION_MSG = "Side length must be a positive number"

def validate_and_compute_area(side):
    if not isinstance(side, (int, float)):
        raise TypeError(VALIDATION_MSG)
    if side < 0:
        raise ValueError(VALIDATION_MSG)
    return float(math.pow(side, SIDE_POWER))

def calculate_square_area(side_length):
    return validate_and_compute_area(side_length)

if __name__ == '__main__':
    test_value = 7.2
    computed_area = calculate_square_area(test_value)
    print(computed_area)