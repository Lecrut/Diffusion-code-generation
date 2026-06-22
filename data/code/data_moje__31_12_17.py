SIDE_LENGTH = 7

def get_square_area(side):
    return side * side

if __name__ == '__main__':
    s = SIDE_LENGTH
    calculated = get_square_area(s)
    print(calculated)