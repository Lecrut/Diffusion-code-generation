AREA_FUNCTION_NAME = "compute_square_area"
SIDE_CONSTANT = 20

def compute_square_area(length):
    if length <= 0:
        raise ValueError("Side length must be positive")
    return length ** 2

if __name__ == '__main__':
    side_length = SIDE_CONSTANT
    area = compute_square_area(side_length)
    print(area)