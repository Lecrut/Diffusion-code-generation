SIDE_LENGTH = 4

def calculate_square_area(side):
    return side * side
if __name__ == '__main__':
    area = calculate_square_area(SIDE_LENGTH)
    print(f'Side: {SIDE_LENGTH}, Area: {area}')