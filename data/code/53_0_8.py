def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    sample_side_lengths = [2, 5, 10]
    for length in sample_side_lengths:
        area = calculate_square_area(length)
        print(area)