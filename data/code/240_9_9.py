SQUARE_SIDE_LENGTH = 3

def calculate_area(side_length):
    return side_length ** 2

if __name__ == '__main__':
    area = calculate_area(SQUARE_SIDE_LENGTH)
    print(area)