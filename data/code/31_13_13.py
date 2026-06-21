SQUARE_SIDE = 20

def compute_square_area(length):
    side_squared = length
    area_result = side_squared * length
    return area_result

if __name__ == '__main__':
    test_side = SQUARE_SIDE
    calculated_area = compute_square_area(test_side)
    print(calculated_area)