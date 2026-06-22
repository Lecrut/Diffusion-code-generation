def calculate_square_area(side_length):
    area = side_length * side_length
    return area

if __name__ == '__main__':
    sample_side = 7
    result_area = calculate_square_area(sample_side)
    print(result_area)