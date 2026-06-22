def calculate_square_area(side_length):
    area = side_length * side_length
    return area

if __name__ == '__main__':
    side_length = 7
    computed_area = calculate_square_area(side_length)
    print(computed_area)