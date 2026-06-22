SIDE_LENGTH = 5

def calculate_square_area(side):
    return side ** 2

if __name__ == '__main__':
    side = SIDE_LENGTH
    area = calculate_square_area(side)
    print(area)