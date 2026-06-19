def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    SAMPLE_SIDE_LENGTH = 7
    area = calculate_square_area(SAMPLE_SIDE_LENGTH)
    print(area)