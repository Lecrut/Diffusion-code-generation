SQUARE1_SIDE = 5
SQUARE2_SIDE = 3

def sum_of_square_areas(side1, side2):
    return side1 ** 2 + side2 ** 2
if __name__ == '__main__':
    total_area = sum_of_square_areas(SQUARE1_SIDE, SQUARE2_SIDE)
    print(total_area)