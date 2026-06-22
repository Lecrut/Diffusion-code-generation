def calculate_square_area(side_length):
    area = side_length ** 2
    return area

if __name__ == '__main__':
    SIDE_LENGTH = 5
    result = calculate_square_area(SIDE_LENGTH)
    print(result)