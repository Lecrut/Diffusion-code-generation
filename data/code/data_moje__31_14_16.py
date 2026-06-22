SQUARE_SIDE = 50

def get_square_area(side):
    area_value = side ** 2
    return area_value

if __name__ == '__main__':
    length = SQUARE_SIDE
    computed_area = get_square_area(length)
    print(computed_area)