SQUARE_AREA_CONSTANT = 2

def compute_square_area(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be positive")
    return side_length ** SQUARE_AREA_CONSTANT

if __name__ == '__main__':
    sample_side_length = 6
    area = compute_square_area(sample_side_length)
    print(area)