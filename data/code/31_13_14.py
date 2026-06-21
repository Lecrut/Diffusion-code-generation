SQUARE_SIDE = 20

def compute_square_area(side):
    if not isinstance(side, (int, float)):
        raise TypeError("Side must be a number")
    return side ** 2

if __name__ == '__main__':
    calculated_area = compute_square_area(SQUARE_SIDE)
    print(calculated_area)