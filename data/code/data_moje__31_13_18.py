SQUARE_SIDE = 20

def get_square_area(side):
    length = side
    width = side
    area_value = length * width
    return area_value

if __name__ == '__main__':
    side_length = SQUARE_SIDE
    computed_area = get_square_area(side_length)
    print(computed_area)