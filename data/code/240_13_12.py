def calculate_square_area(side_length):
    area = side_length ** 2
    return area

if __name__ == '__main__':
    sample_side_length = 6
    computed_area = calculate_square_area(sample_side_length)
    print(computed_area)